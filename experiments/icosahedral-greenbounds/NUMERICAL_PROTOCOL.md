# Executed numerical protocol and reconstruction limits

Base ce89a9cd15439463d9a64d983d91c22ea4368726; limiting exposed case seed10422-0-boundary2 from the frozen jointwindow cases.json, nu=.05,beta=.05,c_f=.001,T=100. Original alpha=.1 pulse, housing energy E_h<=E_p/40000 and80% breathing screen unchanged. All targets and prior adverse phases were development data. No new mechanical parameter fit.

1. Original MountLoss solve: DOP853 rtol2e-12,atol2e-14. Normal step1/20, fine step1/40. Retain all560 mechanical states. The geometry originates in Q(sqrt5); flow is real and numerical.
2. Normal reference: full-state cubic Hermite through state and ODE derivative nodes. Fine amendment: cubic positional Hermite through q,v nodes; define v=q' exactly and ignore diagnostic heat in linearization. This changes representation as well as grid/tolerance; it is not an isolated tolerance comparison.
3. Backward Gramian: integrate in tau=T-u, P_tau=A^TP+PA+l^Tl with zero terminal state. Trace integrals use diagonal P_vv/M/T, grouped1+39+150+90. Normal tolerances2e-7/2e-11; fine2e-8/2e-12. Sample201times. Exact identities are in GREEN_IDENTITY.md.
4. Normal forward: W'=A W, W(0)=B,560x180. Integrate h^T h/T, h^T signal/T and signal^2/T as ODE states, h=lW, rtol2e-9/atol2e-11. Sample1001times for raw/centered/aligned primary norms. Existing convex trust-region routine minimizes the reference-plus-linear mean-volume RMS over all180 initial phases.
5. Exact geometry: interpret retained primary q,v float64 nodes as exact dyadic rationals. Exact13-point centering,3x3 Gram Gershgorin bounds and cubic Bernstein control hulls certify the defined reference curves continuously. This does not enclose their proximity to the original ODE.
6. Four source checks: deterministic normalized direction in each group, entries sin(k)+.3cos(2k),k starting1, with source envelope sin(pi*u/T)^2*cos(omega*u),omega=(1.1,2.3,5.7,3.9). Integrate full linear source response, output RMS and input L2 squared norms at5e-10/2e-13.
7. An extra fifth source consisting of negative reference acceleration defect was interrupted after350.67 CPU seconds without result. Preserve this as INTERRUPTED_WITHOUT_RESULT, not a failed physical/model test. Replace its flow diagnostic with composite3/5-point Gauss on every fine interval for each mass-normalized defect L2 norm. These remain numerical estimates.
8. Post-exposure diagnostic: quintic positions matching original q,v,a at fine nodes, velocity=position derivative. Composite3/5-point Gauss defect norms only. No new Gramian or exact geometry certificate was obtained for this alternative.

Internal time u,edge length and energy scales remain uncalibrated. Modular clocks/prime-factor techniques are N/A: there is no defined divisibility/register question. Primary centering uses Euclidean arithmetic coordinates; force channels use the distinct mass metric.

## Preservation

Three exact original NPZ byte sequences and selected numerical observations survived the workspace outage. Full raw JSON/CSV, original executed scripts, full backward P(0) matrices, receipt and local capture were not published before the outage. The selected compact NPZ includes forward Gram/cross/reference-RMS/adverse phase/final tangent/B and normal/fine initial housing Grams. Large backward P(0) matrices were generated but are not in this capture.

The observations file is explicitly transcribed from successful tool outputs; it is not presented as the original output file. The new geometry recheck script is reconstruction work and NOT_RUN. Recover the original worktree or reproduce from the frozen base before completing the research PR. Do not treat repository integrity CI as a numerical reproduction.
