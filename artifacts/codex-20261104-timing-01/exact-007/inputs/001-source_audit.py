#!/usr/bin/env python3
"""v0.7 bounded source-dependency audit; negative findings are scoped, not exhaustive."""
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).with_name('source_audit_sources')

def main():
    manifest=json.loads((ROOT/'manifest.json').read_text())
    texts={}
    for s in manifest['sources']:
        raw=(ROOT/s['snapshot']).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==s['sha256']
        texts[s['id']]=raw.decode()
    anchors={
      'ledger':['Q169','Q173','gate-transition receipt'],
      'pachner-trigger-lift':['new assumptions','reserve creation','not** a consequence of Q170'],
      'pachner-event-actuator':['No source row supplies an equation','not a derived UD actuator'],
      'qpb1-native-events':['added observer hypothesis','not a source-derived timing law'],
      'qpb1-unit-preparation':['phase rotations preserving','Choosing the normalized representative'],
      'qpb1-finite-window':['when every gap is','at most T_plus/M'],
      'graphite-endogenous-gate':['not ledger-derived','No intrinsic switching time'],
      'pachner-current-metric':['No event trigger','two static memory coordinates'],
      'g05-g06-joint-proof':['no native event time or physical time is identified']}
    for key,terms in anchors.items():
        for term in terms:
            assert term.lower() in texts[key].lower(),(key,term)
    p=Path(__file__).with_name('audit.py')
    spec=importlib.util.spec_from_file_location('timing',p)
    a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
    d=a.main(return_setup=True)
    cp=d['c'][:];cp[3]+=Q(1,4)
    g=a.scalar(d['G'],cp)
    assert g==Q(9,10)
    assert Q(9,10)-g==0
    assert Q(1)-g==Q(1,10) # same state/generator, different assumed reserve
    zero=[Q(0)]*23
    assert a.lin.mvec(d['Ao'],zero)==zero
    assert a.scalar(d['G'],zero)==0
    assert Q(9,10)-a.scalar(d['G'],zero)==Q(9,10) # no zero crossing at all
    assert Q(1,2000)<=Q(1,1000)<Q(1,100)
    # Endpoint phase aliases: theta and theta+2*pi*n have identical sin/cos.
    # This symbolic periodicity is the sampling no-go, not a floating test.
    result={
      'version':'v0.7','evidence':['SOURCE_AUDIT','EXACT_CONDITIONAL','OPEN'],
      'source_revision':manifest['revision'],'bound_sources':len(texts),
      'binding_checks':'SHA-256 and declared excerpt anchors PASS; not an absence proof',
      'event_anchor':{'status':'SOURCE_BLOCKED_AUTONOMOUS; CONDITIONAL_PROTOCOL_AVAILABLE',
          'finding':'Q169 is fixed-complex flow; Q173 gates supplied couplings. Candidate reserve first-entry and event map can define an anchor once posited, but are not selected by those rows.'},
      'phase_step':{'status':'SOURCE_BLOCKED_NATIVE_LAW; DESIGNABLE_ACQUISITION',
          'finding':'Existing sampling bounds assume a gap; continuous generator alone permits meshes 1/2000 and 1/100 and selects neither.'},
      'native_event_observer':{'status':'TYPED_NONTRANSFER',
          'finding':'K4 edge quadrature observer is added, uses another carrier and phase convention, and does not identify this bipyramid move/preparation or its sample-phase law.'},
      'exact_counterexamples':{'same_preparation_reserve_choice':['R=9/10:F=0','R=1:F=1/10'],
          'zero_state':'fixed for Q169 and no reserve crossing for R=9/10',
          'alternative_sampling_meshes':['1/2000 admitted','1/100 outside required ceiling'],
          'endpoint_winding_alias':'theta+2pi*n has identical reference endpoints'},
      'preserved':'all v0.1-v0.6 conditional algebra, classifiers, and their declared hypotheses',
      'frozen_claim':'native autonomous startup or physical experimental readiness from this package',
      'reopening_inputs':['state-defined move/preparation plus source-selected reserve/actuator or a declared external preparation protocol',
          'observer/sampling update with a proved per-step accumulated phase bound or a no-missed-crossing detector contract',
          'relative calibrated signed channel map and error receipts'],
      'limitations':['nine selected documents plus bounded keyword scan; no exhaustive archive/PDF search',
          'source classification is constructor reading, not machine proof of global absence',
          'no cross-carrier phase transfer or physical clock inferred'],
      'physical_promotion':0}
    print(json.dumps(result,indent=2));return result

if __name__=='__main__':
    main()
