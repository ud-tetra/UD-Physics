#!/usr/bin/env python3
"""Byte-identified source coefficient case for the UD phase response audit.
The 150 gain errors and 30 housing weights are serialized as alternating pairs,
expanded canonically to check archived coefficient digest.
"""
from pathlib import Path
import sys, json, hashlib
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from nonaffine_audit import Mechanical,R2
EXPECTED_SHA='8c4d98b69171792190178b12b10a0648ca69aa545a750d3836963747015e98fd'
SOURCE_COMMIT='1e6e0f2abe3fa234919c5a6701547883a807b3e5'
SOURCE_BLOB='419230bb31596cb75b4de2dddd47b281fa02fa47'
SOURCE_PATH='artifacts/icosahedral-jointwindow-20261022-a1/jointwindow-001/files/cases.json'
def case():
    p=json.loads((HERE/'frozen_case.json').read_text())
    p['ratio_error']=p['ratio_error']*75
    p['housing_weights']=p['housing_weights']*15
    j={k:p[k] for k in ['primary','ratio_error','beta','cf','omega_h','housing_weights']}
    s=hashlib.sha256(json.dumps(j,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert s==EXPECTED_SHA, ('source coefficient hash discrepancy',s)
    return p
class FrozenMechanical(Mechanical):
    def __init__(self,nu=.05):
        p=case()
        super().__init__(nu=nu,beta=p['beta'],cf=p['cf'],primary_pattern='uniform')
        self.m=np.array(p['primary']['m']);self.g=np.array(p['primary']['g']);self.k=np.array(p['primary']['k'])
        self.hw=np.array(p['housing_weights']);self.gain=1+np.array(p['ratio_error'])
        self.M=np.r_[1.,np.repeat(self.m/R2,3),np.full(150,.1*2),np.repeat(.4*self.beta*self.hw/R2,3)]
        self.mh=.4*self.beta*self.hw/R2;self.kh=self.mh*100
        self.G=np.zeros((150,42));indices=np.arange(150)
        from nonaffine_audit import pairs
        self.G[indices,pairs[:,0]]=1
        self.G[indices,pairs[:,1]]=-self.gain
        self.pattern=p['id']
if __name__=='__main__':
    print('PASS',case()['id'],EXPECTED_SHA)
