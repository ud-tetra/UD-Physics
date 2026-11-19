"""Frozen exact scorer. No fixture key is consumed in the classify phase."""
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

PROTOCOL = 'UD-CAP-BENCH-v0.1'
IDS = tuple(f'B{i:02}' for i in range(1,17))
V = {'x':(1,0),'y':(F(-1,2),1),'c':(0,1)}
ETA = F(1,100)
RADIUS = 2*(6*ETA+16*ETA**2+F(1,32))


def need(ok, message):
    if not ok:
        raise ValueError(message)


def canon(x):
    return json.dumps(x,sort_keys=True,separators=(',',':')).encode()


def digest(x):
    return hashlib.sha256(x).hexdigest()


def rat(x):
    need(type(x) in (str,int),'Use integer or exact rational strings')
    return F(x)


def grade(block):
    receipts={}
    if (rat(block['timing_bound_over_T']) > F(1,10000) or
        block['independent_certificates_ok'] is not True):
        return {'call':'ABSTAIN_CERTIFICATE'}
    shots=block['shots']
    need(set(shots)=={f'{k}{s}' for k in V for s in ('-','0','+')},'Wrong shot inventory')
    for k,v in V.items():
        vals=[]
        for label,sgn in (('-',-1),('0',0),('+',1)):
            row=shots[k+label]
            for field,target in [('initial',(0,0)),('loaded',tuple(sgn*x for x in v)),
                                 ('returned',(0,0))]:
                coords=row[field]
                need(len(coords)==2 and all(len(x)==2 for x in coords),'Bad charge shape')
                for (q,u),ref in zip(coords,target):
                    q,u=rat(q),rat(u)
                    need(u>=0,'Negative charge bound')
                    if abs(q-ref)+u>ETA:
                        return {'call':'ABSTAIN_CHARGE'}
            w,r,uw,ur=map(rat,(row['load_work'],row['return_work'],
                                 row['load_uncertainty'],row['return_uncertainty']))
            need(min(uw,ur)>=0,'Negative work uncertainty')
            if max(uw,ur)>F(1,512):
                return {'call':'ABSTAIN_INTEGRATION'}
            # Both initial and returned energies are bounded by 4η² W*
            # per endpoint. 8η² conservatively bounds their difference.
            if abs(w+r)+uw+ur+8*ETA**2>F(1,128):
                return {'call':'ABSTAIN_CLOSURE'}
            vals.append(w)
        receipts[k]=(vals[0]+vals[2])/2-vals[1]
    s=receipts['c']-receipts['y']
    lo,hi=s-RADIUS,s+RADIUS
    call='CANDIDATE_SIGN' if lo>0 else 'UNIFORM_SIGN' if hi<0 else 'ABSTAIN_SIGN'
    return {'call':call,'S_over_Wstar':str(s),'interval':[str(lo),str(hi)],
            'work_over_Wstar':{k:str(w) for k,w in receipts.items()}}


def classify(data):
    need(data['protocol']==PROTOCOL,'Wrong protocol')
    c=data['commitment']
    need(len(c)==64 and all(s in '0123456789abcdef' for s in c),'Bad commitment')
    blocks=data['blocks']
    need(tuple(b['id'] for b in blocks)==IDS,'Incomplete or reordered blocks')
    for b in blocks:
        need(rat(b['timing_bound_over_T'])>=0,'Negative timing bound')
    return {'protocol':PROTOCOL,'commitment':c,'input_hash':digest(canon(data)),
            'calls':{b['id']:grade(b) for b in blocks}}


def score(predictions,key,frozen_predictions_sha):
    need(digest(canon(predictions))==frozen_predictions_sha,'Prediction seal mismatch')
    need(key['protocol']==predictions['protocol']==PROTOCOL,'Wrong protocol')
    need(digest(canon(key))==predictions['commitment'],'Wrong key commitment')
    salt=key['salt_hex']
    need(len(salt)==64 and all(s in '0123456789abcdef' for s in salt),'Bad salt')
    arms=key['arms']
    need(set(arms)==set(IDS) and set(predictions['calls'])==set(IDS),'Wrong ID set')
    counts={}
    for arm,expected in [('candidate','CANDIDATE_SIGN'),('uniform','UNIFORM_SIGN')]:
        b=[predictions['calls'][k]['call'] for k in IDS if arms[k]==arm]
        need(len(b)==8,'Expected exactly eight blocks per arm')
        counts[arm]={'correct':b.count(expected),'abstain':sum(s.startswith('ABSTAIN_') for s in b)}
        counts[arm]['wrong']=8-counts[arm]['correct']-counts[arm]['abstain']
    return {'counts':counts,'pass':all(v['correct']>=7 and v['wrong']==0 for v in counts.values())}


if __name__=='__main__':
    mode,path,*args=sys.argv[1:]
    a=json.loads(Path(path).read_text())
    if mode=='classify' and not args:
        result=classify(a)
    elif mode=='score' and len(args)==2:
        result=score(a,json.loads(Path(args[0]).read_text()),args[1])
    else:
        raise SystemExit('classify INPUT | score PREDICTIONS KEY SEALED_CANONICAL_SHA256')
    print(json.dumps(result,indent=2))
