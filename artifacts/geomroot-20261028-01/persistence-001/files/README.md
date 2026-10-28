# One-hot native K4 root: exact conservative persistence test

**Status:** EXACT/CONDITIONAL finite incidence evolution with an assumed one-hot initial preparation; no physical time, material contact, damping or cube selection. Independent physics review NOT_RUN; physical promotion 0.

## Question and generator

The [native selector audit](../geometry-native-selector/README.md) shows that a fully `S4`-invariant state cannot uniquely choose a root. Supply the minimal asymmetric initial condition `x(0)=e0` on the four K4 vertex amplitudes, with oriented edge amplitudes `y(0)=0`, and ask whether a root persists under the existing free `0<->1` support generator. This is an explicitly prepared `S3`-invariant branch, not a spontaneous root derived from an invariant packet. Use ascending edge orientations, `B1:C1(K4;R)->C0(K4;R)`, the ordinary unit chain metric, and dimensionless time `s`:

`x'=-B1 y,  y'=B1^T x,  S=||x||²+||y||².`

This sign convention matches the [native support-current note](../graphite-native-support-current/README.md). The Q166 vertex-to-edge signed flow is `F_ie=2 B1_ie x_i y_e`; then `(x_i²)'=-sum_e F_ie`, `(y_e²)'=sum_i F_ie`, and `S'=0` exactly. The state amplitudes are signed, while `S` is a nonnegative stock. The free truncation excludes faces, masks, contact drive, open-system reservoirs and dissipative material physics.

## Closed solution and loss of a unique root

The K4 graph Laplacian is `B1 B1^T=4I-J` (where `J` is the 4-by-4 all-ones matrix). Write `c=cos(2s)`, `h=sin(2s)`. The unique solution is

`x0=(1+3c)/4`, `x1=x2=x3=(1-c)/4`, `y=(h/2) B1^T e0`.

Consequently `x0-xi=c` for each `i=1,2,3`, and `x0²-xi²=c(1+c)/2`. A rule that calls the uniquely largest vertex amplitude the root picks `0` only for `c>0`; at the first tie `s=pi/4` all four vertex amplitudes are `1/4`, while three incident edge amplitudes each have magnitude `1/2`. For `pi/4<s<3pi/4`, the three unprepared vertices tie above vertex 0. A squared-stock root rule likewise loses the uniquely maximal original root for `-1<=c<=0` (ties at the endpoints). At `s=pi/2`, `x=(-1/2,1/2,1/2,1/2)` and `y=0`, so all four vertex stocks are equal. The full free state is periodic with period `pi` in `s`; the original branch revives but is not continuously retained.

The exact stock is `S=1`, partitioned between vertices and edges. All vertex/edge stocks and Q166 currents are periodic, so their signed time-averaged derivatives and net transfers over a full cycle vanish. Instantaneous currents can be nonzero and signed; none is an irreversible physical loss or friction force. A *fixed* one-hot contact label could still name root 0 throughout, but that would be an external persistent label rather than selection from the evolving free amplitude or stock.

`replay.py` verifies the integer Laplacian, equations, local stock balances and `S=1` at exact rational circle phases. The solution and tie times are proved by the formulas above; finite samples are not a substitute for the analytic solution.

## Interpretation gate

The [rooted six-sector cube map](../geometry-six-sector-map/README.md) can be conditioned on the prepared label only if a native boundary/contact register retains that label as the free amplitudes redistribute. The [full S4 map](../geometry-s4-full-map/README.md) does not require such a root. This exact free-model result rules out *continuous amplitude-based persistence* of the prepared root under the declared generator; it does not rule out driven, gated, nonlinear or open-system native laws. Q167 masks and Q170 ownership could be explored with their transition stock ledger, but selecting a mask threshold or pinning energy needs an independent source. No factor here determines the geometric `3^(1/6)` area normalization or graphite friction/load response.

Next discriminant: construct one sourced persistent contact/register with an explicit update and power/stock accounting, compare its rooted response to the symmetric map, and derive a physical observable before assigning any coefficient.
