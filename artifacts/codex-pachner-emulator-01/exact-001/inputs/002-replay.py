"""Controlled interface replay. Exact arithmetic; no experimental inputs."""
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
raw = (HERE / "CONTRACT.json").read_bytes()
c = json.loads(raw)
p = HERE.parent / "pachner-timing-budget" / "calibration_startup.py"
spec = importlib.util.spec_from_file_location("startup", p)
startup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(startup)
assert startup.MAX_PHASE_STEP == Q(c["phase_cap"])
assert startup.pair.DELTA == Q(c["per_channel_ceiling"])
assert startup.pair.REFERENCE_WINDOW == tuple(map(Q, c["reference_window"]))
assert startup.pair.THRESHOLD == Q(c["threshold"])
g, b, eta, n = (Q(c[k]) for k in
                ("gain_bound", "offset_bound", "noise_budget", "injected_noise"))
bounds = (Q(0), Q(0), Q(0), g, g, b, b, eta)

def measure(mode, u, polarity, index):
    # Independent scalar-series implementation of the declared analytic source.
    assert 0 <= u <= Q(1,20)
    m = {"FULL": 5, "PROJECTED": 3}[mode]
    w = -sum(Q((-m)**j, 4*factorial(2*j))*u**(2*j) for j in range(12))
    y = sum(Q(2*(-5)**j, factorial(2*j+1))*u**(2*j+1) for j in range(12))
    rw = Q(m**12, 4*factorial(24))*u**24
    ry = Q(2*5**12, factorial(25))*u**25
    assert max(rw,ry) <= Q(c["series_remainder_budget"])
    assert n+(1+g)*max(rw,ry) <= eta
    noise = n*polarity*(-1 if index % 2 else 1)
    return ((1+g*polarity)*w + b*polarity + noise,
            (1-g*polarity)*y - b*polarity - noise)

def run(mode, rate, pattern, polarity):
    latch = startup.StartupLatch(bounds=bounds)
    anchor = measure(mode,Q(0),polarity,0)
    assert latch.reset_at_event(*anchor, "synthetic:phase-zero") == "ARMED"
    trace = []
    u = Q(0)
    for j in range(c["max_samples"]):
        step = rate*pattern[j%len(pattern)]
        u += step
        w,y = measure(mode,u,polarity,j+1)
        result = latch.observe(w,y,step)
        trace.append((str(step),str(w),str(y),result))
        if result != "WAITING":
            return result,trace
    return "NO_DECISION",trace

cases = []
for mode in ("FULL","PROJECTED"):
    for rate in map(Q,c["rates"]):
        for i,pattern in enumerate(c["interval_patterns"]):
            for polarity in c["sensor_polarities"]:
                result,trace = run(mode,rate,list(map(Q,pattern)),polarity)
                cases.append(dict(expected=mode,observed=result,rate=str(rate),
                                  pattern=i,polarity=polarity,samples=len(trace)))
counts = {m:sum(row["expected"]==row["observed"]==m for row in cases)
          for m in ("FULL","PROJECTED")}
wrong = sum(row["observed"] in counts and row["observed"] != row["expected"]
            for row in cases)
abstain = sum(row["observed"] not in counts for row in cases)
# Matched-generator null: replace the challenger with the baseline law.
# This tests differential agreement, not a third class or general null detection.
null_a = run("FULL",Q(1),[Q(1,4000)],1)
null_b = run("FULL",Q(1),[Q(1,4000)],1)
assert null_a==null_b and null_a[0]=="FULL"

latch = startup.StartupLatch(bounds=bounds)
latch.reset_at_event(Q(-1,4),Q(0),"synthetic:phase-zero")
bad_step = latch.observe(Q(-1,4),Q(1,100),2*startup.MAX_PHASE_STEP)
try:
    startup.StartupLatch(bounds=(*bounds[:-1],2*startup.pair.DELTA))
except ValueError as e:
    assert "budget" in str(e)
    bad_cal = "REJECTED_CALIBRATION"
else:
    raise AssertionError("over-budget calibration admitted")
bad_event = startup.StartupLatch(bounds=bounds).reset_at_event(
    Q(0),Q(0),"synthetic:bad-envelope")
stalled,_ = run("FULL",Q(0),[Q(1,4000)],0)
controls = dict(phase_cap=bad_step,calibration_cap=bad_cal,
                bad_event=bad_event,stalled=stalled)
assert controls == c["acceptance"]["abstention_controls"]
assert counts == {m:c["acceptance"][m+"_correct"] for m in counts}
assert wrong==c["acceptance"]["wrong"] and abstain==0
assert c["acceptance"]["matched_continuation_nulls"] == 1
print(json.dumps(dict(contract_sha256=hashlib.sha256(raw).hexdigest(),
                      correct=counts,wrong=wrong,abstentions=abstain,
                      matched_null="IDENTICAL_TRACE_AND_LABEL",
                      abstention_controls=controls,cases=cases),indent=2))
