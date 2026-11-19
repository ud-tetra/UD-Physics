"""Synthetic workflow controls; fixture labels do not enter classify()."""
from copy import deepcopy
from bench_score import IDS, PROTOCOL, V, canon, classify, digest, score, F
import json


def run():
    arms={k:('candidate' if i%2 else 'uniform') for i,k in enumerate(IDS)}
    key={'protocol':PROTOCOL,'salt_hex':'42'*32,'arms':arms}  # synthetic only
    data={'protocol':PROTOCOL,'commitment':digest(canon(key)),'blocks':[]}
    for k in IDS:
        w={'x':F(1),'y':F(5,4),'c':F(3,2) if arms[k]=='candidate' else F(1)}
        shots={}
        for label,v in V.items():
            for suffix,sign in [('-',-1),('0',0),('+',1)]:
                shots[label+suffix]={'initial':[[0,0],[0,0]],'returned':[[0,0],[0,0]],
                      'loaded':[[str(sign*x),0] for x in v],
                      'load_work':str(sign**2*w[label]),'return_work':str(-sign**2*w[label]),
                      'load_uncertainty':'1/1024','return_uncertainty':'1/1024'}
        data['blocks'].append({'id':k,'timing_bound_over_T':'1/20000',
                               'independent_certificates_ok':True,'shots':shots})
    def test(data):
        p=classify(data)
        return p,score(p,key,digest(canon(p)))
    p,clean=test(data)
    assert clean['pass']
    bad=deepcopy(data)
    bad['blocks'][0]['shots']['c+']['return_work']='-9/10'
    b,one=test(bad)
    assert one['pass'] and b['calls'][IDS[0]]['call']=='ABSTAIN_CLOSURE'
    bad['blocks'][2]['shots']['y-']['loaded'][0][1]='1/50'
    b,two=test(bad)
    assert not two['pass'] and b['calls'][IDS[2]]['call']=='ABSTAIN_CHARGE'
    wrong=deepcopy(data)
    wrong['blocks'][0]['shots']=deepcopy(data['blocks'][1]['shots'])
    _,wrong_score=test(wrong)
    assert not wrong_score['pass'] and wrong_score['counts']['uniform']['wrong']==1
    wrong_key={**key,'salt_hex':'43'*32}
    for k,h in [(wrong_key,digest(canon(p))),(key,'0'*64)]:
        try:
            score(p,k,h)
        except ValueError:
            pass
        else:
            raise AssertionError('Altered key or seal admitted')
    return {'clean':clean,'one_abstention':one,'two_same_arm_abstentions':two,
            'wrong_call':wrong_score,'tampered_key_and_seal':'rejected'}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
