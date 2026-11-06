# Full-new versus projected memory evolution: preparation audit v0.2

EXACT / CONDITIONAL. Continues PR #308, source commit
`39d7c2d48a7670ae5b9d94402dcfd33b922d6e73`. No empirical targets.
This amendment preserves the v0.1 mask comparison and its immutable capture.
It asks a DIFFERENT question: at the same event, does full new-carrier flow
differ from the projected flow, keeping the mask the same between hypotheses?

## Carrier and two laws

Use the objects and signed bases from [v0.1](README.md). The common ambient
carrier is the 27-dimensional target plus the rank-two memory subspace.
The event inclusion is Tq=(Mq,Pq), with T^T T=H.
Full evolution is diag(A_h,0); projected evolution is T exp(K_h t),
K_h=H^-1 M^T A_h M. The full branch keeps the memory record constant;
the projected branch need not do so for arbitrary preparations.
Both laws conserve total target-plus-memory unit stock, and both norms are
bounded by 5 in their corresponding isometric coordinates. No physical time,
instrument or reason selecting one law is supplied.

## EXACT obstruction for the original preparation

Let c_0 be the v0.1 unit face-012 plus unit edge-01 witness.
Define E_h=A_h M-M K_h. Fraction arithmetic verifies, for k=0,...,22,

E_h K_h^k c_0=0, and P K_h^(k+1)c_0=0,

for both all-active and single-edge masks. Their old-coordinate cyclic
subspaces span{c_0,K_h c_0,...} have dimensions 5 and 7, respectively.
Cayley-Hamilton in dimension 23 extends both zero identities to every power.
Consequently the analytic exponential series gives, for every real t,

exp(A_h t)M c_0 = M exp(K_h t)c_0,
P exp(K_h t)c_0 = P c_0.

Thus every target boundary readout agrees EXACTLY between the two
continuations for the original nominal preparation. This is not a numerical
resolution limit. A perturbation set containing zero error contains this
indistinguishable witness; hence it cannot support a uniform full/projected
classifier. The earlier v0.1 discriminator compares two MASKS within the
projected law and remains valid.

## Deliberately changed probe

To reopen the comparison, add alpha e_3 to the OLD vertex register,
alpha=1/4. This is a new signed preparation, not spontaneous/native selection.
Use both hypotheses with ALL vertex-edge contacts active.
No edge mask is inferred from the probe.
The reserve and nominal crossing slope remain R=g=9/10, gdot=-3.
Old squared norm becomes 33/16; event target-plus-memory stock is 237/80.

The born internal edge (3,4) has full-flow derivative alpha, whereas its
projected amplitude is identically zero because that row of M is zero.
That internal register is not claimed to be a boundary sensor.

Use instead the boundary vertex contrast W=x_4-x_3.
For full minus projected, its derivatives through order 3 are
(0,0,1/2,0). Thus Delta W(t)=alpha t^2+O(t^3).
The original c_0 component cancels exactly by the preceding theorem.
Only alpha T e_3 contributes to the difference, and ||T e_3||=1.
Each remaining scalar third derivative is bounded by sqrt(2)*5^3*alpha,
so the combined Taylor remainder has magnitude <=60alpha t^3.
Hence

Delta W(t)>=alpha t^2-60alpha t^3>=alpha t^2/2
for 0<t<=1/120.

On nominal sample times s in [1/240,1/120], this gives
Delta W>=1/460800. Compare one signed reading with the midpoint of the
two exact nominal predictions; the greater value corresponds to full flow.
This rule requires fixed signed preparation and registered vertex labels.

## Same error model, rechecked constants

Prepare at nominal time -1/600 with Euclidean error <=epsilon,
constant reserve error <=r, sample jitter <=nu, scalar readout error <=eta.
The pre-event generator and event transport are unchanged.
The nominal commutator bound is still ||G A_o-A_o G||<=15.
Now |F''|<=150*(33/16), and F'>12/5 on [-1/600,1/600].
Since sqrt(33/16)<3/2, the derivative perturbation remains bounded by
45epsilon+15epsilon^2 and the value error by d=r+5epsilon.
For epsilon<=1/1000, d<=1/1000, the actual F'>2 and the endpoints
have opposite signs. There is one local inward zero, with
|t_star|<=d/2, just as in v0.1.

The event-state error remains <=2epsilon+12|t_star| because
(5/2)*25*(33/16)<144. Both post-event laws are ambient isometries.
The contrast preparation contribution is <=3epsilon+17|t_star|.
The nominal time derivative bound is <13, since
25*2*(237/80)<169. Including timing and scalar error gives the SAME form:

total scalar error <=78epsilon+15r+13nu+eta.

A sufficient condition for the NEW full/projected probe is

78epsilon+15r+13nu+eta <= 1/1000000 < 1/921600,

where the latter is half the new separation floor.
This implies the coarse crossing domain and that the sample follows the
actual event. The complete concrete example from v0.1 still passes:
epsilon=1/200000000, r=1/100000000, nu=1/100000000,
eta=1/4000000, with weighted budget 23/25000000.

This comparison assumes an immediate event and fixed all-active continuation.
A gate ramp is another constitutive law with different predictions.
The state-dependent reserve is not a source-derived actuator; clock scaling,
instrument calibration, independent review, basin attraction and physical
promotion remain open. Numerical midpoint implementation error must be
included in eta; no floating midpoint implementation was tested.

## Reproduction

Run `python3 -B experiments/pachner-timing-budget/comparison.py`.
This verifies the zero-defect cyclic subspaces, probe derivatives, stocks,
and rational inequalities used above. The v0.1 audit now accepts a setup-only
return for reuse; its normal output remains byte-for-byte unchanged.

Independent next discriminant: implement exact rational Taylor prediction
enclosures for the two probe readouts and verify a finite-computation classifier,
including its midpoint rounding/truncation error.
