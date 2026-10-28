# Endpoint-local odd readout: a covariance support bound

**EXACT/CONDITIONAL** support-overlap theorem; **NUMERICAL** evaluation on the exposed conventional registered graphite Hessian. This is a scoped locality test, not a friction measurement or a native UD source derivation. Physical promotion 0; independent physics review NOT_RUN.

## Question and typed setting

The [joint quadrature/contact construction](../graphite-joint-quadrature-contact/README.md) matches the conventional conservative bond process with the target-selected odd map $r=B^TK^{-1/2}x'/\sqrt a$. Can a linear odd readout at bond $e$ use **only its two endpoint site velocities** and still reproduce the full stationary bond covariance? How far does an exact support argument extend when the neighborhood grows?

Use the registered 14-site, 21-edge oriented honeycomb incidence $B:\mathbb R^{21}\to\mathbb R^{14}$ and positive conventional stiffness $K$ in meV/Å² per mean upper atom. The physical height proxy $q=B^Tx$ has covariance $\Theta_{\rm bar}Q$ with $Q=B^TK^{-1}B$ and $\Theta_{\rm bar}=k_BT/14$. As in the previous **assumed** positive oscillator, the site velocity has isotropic canonical covariance $\operatorname{Cov}(x')=a\Theta_{\rm bar}I$, $a=14\tau^2/m$. A candidate odd observable is $r=D x'/\sqrt a$, with $D:\mathbb R^{14}\to\mathbb R^{21}$. Thus $\operatorname{Cov}(r)/\Theta_{\rm bar}=DD^T$. No value of $m$, $\tau$, or the measured loss is needed for the normalized comparison.

For radius $R\geq0$, allow row $D_e$ to be supported on $N_R(e)$, the site vertices within graph distance $R$ of either endpoint of bond $e$. Radius zero allows two arbitrary real coefficients per edge (42 coefficients before constraints); it does **not** force the incidence signs. For any two edges $e,f$ whose allowed site sets do not overlap,

$$N_R(e)\cap N_R(f)=\varnothing\quad\Longrightarrow\quad(DD^T)_{ef}=0.\tag{1}$$

Define the symmetric mask $Z_R(e,f)=1$ precisely on those disjoint-support pairs and zero elsewhere. Entrywise orthogonality gives the exact lower bound, for **every** real $D$ in this support family,

$$\frac{\|DD^T-Q\|_F}{\|Q\|_F}\ \geq\
\frac{\|Z_R\odot Q\|_F}{\|Q\|_F}.\tag{2}$$

This is a covariance bound at lag zero. Matching the entire two-time spectrum also requires matching lag zero, so the same obstruction rules out an exact all-lag match under these assumptions. It does not constrain the even local proxy $q=B^Tx$: its site heights have correlated covariance $\Theta_{\rm bar}K^{-1}$, whereas the assumed odd site velocities are isotropic.

## Exact support count and numerical target evaluation

In this 14-site graph, each bond meets four other bonds and is disjoint from 16; hence there are $21\cdot16/2=168$ unordered disjoint pairs out of $\binom{21}{2}=210$. The [integer carrier replay](replay_local.py) checks this count from the incidence matrix. All 168 corresponding $Q_{ef}$ in the registered numerical model are nonzero (absolute magnitudes $3.77527\times10^{-4}$ to $6.55722\times10^{-4}$ Å²/meV). Equation (2) yields a **69.0899466%** relative Frobenius lower bound for every endpoint-local odd readout in the stated isotropic-velocity model. The graph-average $\bar K$ still has a **69.0674961%** bound, although its bond-variance source cancels. The obstruction reflects correlated conventional bond fluctuations, not merely the small registry defect.

Across the archived nominal and alternate-step Hessians at $-2.5,0,+2.5$ MPa relative pressure, the radius-zero bound ranges from **69.0894096% to 69.0904752%**. These are numerical sensitivity checks within one reconstructed conventional model, not uncertainty intervals for an experiment. At radius one, every pair of allowed neighborhoods intersects on this small quotient, so the support mask is empty and equation (2) yields zero. **Zero bound is inconclusive**: it does not construct a one-hop readout or show that one can match $Q$.

## Why the variance port alone is insufficient

The uniform local odd gradient $D=B^T$ has bond variance 2 at every edge, and the assumed harmonic variance port cancels. If each edge receives a separate **target-fitted** scale $c_e=\sqrt{Q_{ee}/2}$, then $D=\operatorname{diag}(c_e)B^T$ exactly reproduces all 21 diagonal weights and the earlier rank-two proxy port. Yet its full covariance differs from $Q$ by **87.8344%** in relative Frobenius norm. The scales were chosen using the exposed $Q$; their diagonal success is neither an independently derived UD source nor a friction residual. The 69.09% bound applies even to the larger arbitrary 42-coefficient endpoint family.

This rules out only a linear, instantaneous endpoint-supported odd map with isotropic site-velocity covariance and the full registered bond covariance as target. A correlated kinetic metric, an edge bath with shared states, a temporal filter, a one-hop spatial map, or a different material observable changes the premises and must specify its reciprocal energy and preparation. No measured signed friction, complex loss, contact transfer, angle selection, or physical load slope follows. The 21.8°/38.2° pair remains conventionally accounted for by the $(2,1)$ triangular coincidence.

Run `python3 experiments/graphite-local-readout-bound/replay_local.py` from repository root. [Results](LOCAL_RESULTS.json), [mathematical receipt](../../candidates/graphite-local-readout-bound/mathematical_receipt.json), and [immutable capture](../../artifacts/graphlocal-20261028-01/local-001/manifest.json) preserve the support count, model inputs, and sensitivity checks.
