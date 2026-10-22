# Session icosahedral-free3d-20261022-a1

Boot attempt: 2026-10-22T18:50:26.841426+00:00

Runtime: Codex; model identifier unknown; Git/compute and GitHub connector write

Task: integration-icosahedral-free3d-20261022

Goal: Remove radial guides and test full3D equilibrium and breathing stability,rigid motions and imperfection sensitivity

Ownership: UNCLAIMED until remote claim acquisition succeeds.

## 2026-10-22T18:50:26.921898+00:00

Created candidate icosahedral-free3d: Does the passive central volume response survive releasing radial guides,including angular/shear motion and small imperfections?

## 2026-10-22T18:57:54.507577+00:00

EXACT: free centre+12 shell points+scalar gives40 coordinates,rank34 and six rigid null directions;positive model energy gives orbital equilibrium stability modulo Euclidean motions. Exact Q(sqrt5) LDL certificate gives all-phase nonrigid stiffness>=1/10 for symmetric A0<=1/10. NUMERICAL:80-state breathing matches analytic within9.06e-10;normal energy-amplitude gain1.267 at u400.16 seeded property probes retain mean-volume RMS>=99.61% (±1%) and97.83% (±5%). Hub-relative cell signal leakage max3.11%/18.62%; shell-mean-centre leakage1.66%/8.84%,showing repartition versus shape must be distinguished. Figure inspected. Added exact projection check initially had an int/Q5 coercion TypeError; corrected and certificate rerun successfully.

BOOT/ownership: current AGENTS/state/preceding mechanicalreport read at verifiedbase fbf35ff97a148b42dc57322c71bd905aec2adff5;standing canonicalinstructions/method/concurrency/artifactprotocol applied. All12 prior liveclaims released,noopenPRs. New claim c99009f59ea2040a7d051588279f2b176e30325a acquired before substantiveedits;isolatedworktree. Unknownmodelidentifier;Git/compute andconnectorwrite available. Exact/numerical domains,units andhypotheses recorded inreceipt. Suppliedledger Q139/Q144-145/Q151-152 andgovernance proposalstatus inspected. Unavailable Gap2 image is not used.

First campaign completed. Observed hub-relativevolumemismatch prompted separate shell-mean-centre/proper-fit shapereadouts and two worst-probe refinements;complete finalcampaign rerun beforecapture. Exactcertificate initially passed,then added rigid-projection identities hit a fieldcoercion programmingerror;fixed andsuccessful finalcertificate rerun. No failedoutcomes promoted. Figure inspected. Capture/validation follow.

## 2026-10-22T19:01:50.295612+00:00

Captured artifacts/icosahedral-free3d-20261022-a1/free3d-001 (NUMERICAL): Exact free3D rigidity/stiffness and finite transverse/nonlinear imperfection checks;hub partition separated from shell shape

Captured free3d-001 withseven explicitinput copies andsix outputs. Validator PASS59records;all16tooling tests PASS. Readyforfocused integration;exact/numerical scope retained.
