"""Direct state-vector evolution; no scalar source from the original harness."""
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
raw = (here / "MATRIX_CONTRACT.json").read_bytes()
cfg = json.loads(raw)
assert hashlib.sha256((here / "CONTRACT.json").read_bytes()).hexdigest() == cfg["parent_contract_sha256"]
seed = bytes.fromhex(Path(sys.argv[1]).read_text().strip())
assert len(seed) == 32
p = here.parent / "pachner-timing-budget" / "calibration_startup.py"
spec = importlib.util.spec_from_file_location("startup", p)
startup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(startup)
a, d = startup.pair.load()
c = d["c"][:]
c[3] += Q(1, 4)
M = d["M"]
full = a.lin.mvec(M, c)

def mv(A, v):
    return [sum((x*y for x,y in zip(row,v) if x), Q(0)) for row in A]

def jets(A, v, project):
    coeff = [[], []]
    for k in range(cfg["degree"]+1):
        x = mv(M,v) if project else v
        coeff[0].append((x[4]-x[3])/factorial(k))
        coeff[1].append((x[1]-x[0])/factorial(k))
        v = mv(A,v)
    return coeff

tables = {"FULL": jets(d["An"],full,False),
          "PROJECTED": jets(d["K0"],c,True)}

def eval_poly(coeff,u):
    v = Q(0)
    for x in reversed(coeff):
        v = u*v+x
    return v

g,b,n,eta = (Q(cfg[k]) for k in
             ("gain_bound","offset_bound","noise_amplitude","noise_budget"))
u_max = Q(cfg["max_phase"])
k = cfg["degree"]+1
# Reviewed event norm/readout product < 5/2 and generator norm <= 5.
tail = Q(5,2)*(5*u_max)**k/factorial(k)
assert n+(1+g)*tail <= eta
bounds = (Q(0),Q(0),Q(0),g,g,b,b,eta)
rates = list(map(Q,cfg["rates"]))
intervals = list(map(Q,cfg["intervals"]))
assert max(rates)*max(intervals)<=startup.MAX_PHASE_STEP

def digest(i,j):
    return hashlib.sha256(seed + i.to_bytes(4,"big") + j.to_bytes(4,"big")).digest()

def signed(byte,bound):
    return Q(byte-128,128)*bound

def run(mode,i):
    static = digest(i,0)
    gw,gy,bw,by = [signed(x,lim) for x,lim in zip(static,(g,g,b,b))]
    def read(u,j):
        w,y = (eval_poly(t,u) for t in tables[mode])
        q = digest(i,j)
        return (w*(1+gw)+bw+signed(q[2],n),
                y*(1+gy)+by+signed(q[3],n))
    latch = startup.StartupLatch(bounds=bounds)
    assert latch.reset_at_event(*read(Q(0),0),f"external-emulator:{i}")=="ARMED"
    u = Q(0)
    used = []
    for j in range(1,cfg["max_samples"]+1):
        q = digest(i,j)
        rate,interval = rates[q[0]%len(rates)],intervals[q[1]%len(intervals)]
        step = rate*interval
        u += step
        assert u<=u_max
        w,y = read(u,j)
        result = latch.observe(w,y,step)
        used.append([str(rate),str(interval),str(w),str(y),result])
        if result!="WAITING":
            return result,used
    return "NO_DECISION",used

rows = []
for mode in tables:
    for i in range(cfg["case_count_per_model"]):
        result,trace = run(mode,i)
        rows.append(dict(case=i,expected=mode,observed=result,trace=trace))
counts = {m:sum(r["expected"]==r["observed"]==m for r in rows) for m in tables}
counts["wrong"] = sum(r["observed"] in tables and r["expected"]!=r["observed"] for r in rows)
counts["abstain"] = sum(r["observed"] not in tables for r in rows)
assert counts==cfg["expected"], counts
assert run("FULL",0)==run("FULL",0)
print(json.dumps(dict(contract_sha256=hashlib.sha256(raw).hexdigest(),seed=seed.hex(),
                      counts=counts,remainder_bound=str(tail),cases=rows),indent=2))
