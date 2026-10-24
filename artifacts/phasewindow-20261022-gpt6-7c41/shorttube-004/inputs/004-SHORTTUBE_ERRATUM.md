# SHORTTUBE mathematical notation correction — version 2

**CORRECTION / EXACT / CONDITIONAL.** Supersedes only the intermediate *time-dependent strictness* statements in original immutable run `shorttube-003`. The underlying Duhamel/energy/Gram calculations, final constant inequalities, and conclusion remain unchanged.

## Historical issue retained

The original `SHORTTUBE.md` in captured run `shorttube-003` stated `(1-2u)^3 < V_k(u)/V_k(0) < (1+2u)^3` throughout `0<=u<=2/5`. At `u=0`, the ratio and both envelopes equal exactly one, making the strict version false at the initial instant. Some intermediate point-displacement inequalities likewise used strict `<(2/5)u` at `u=0`, where both sides are zero.

## Corrected statement

For every permitted trajectory and `u∈[0,2/5]`,

```
|X_a(u)-X_a(0)| <= (2/5)u,
||A_ref^(-1)(A(u)-A_ref)||_2 <= 2u <= 4/5 <1,
(1-2u)^3 <= V_k(u)/V_k(0) <= (1+2u)^3.
```

For `u>0`, the inequalities prior to the `4/5` comparison can be made strict using the strict speed majorants. At `u=0`, equality is necessary. The **fixed** bounds are strictly valid throughout the closed interval including `u=0`:

```
1/125 < V_k(u)/V_k(0) < 729/125.
```

The housing-strut uniform bound `ell_ea(u)>13/1500`, full-state continuation through `u=2/5`, all initial phase directions and property-range scope are unchanged. The original 0.1-amplitude u=100 theorem remains OPEN.

## Provenance

Historical `shorttube-003` capture remains immutable and its overly strict intermediate notation is preserved as an auditable error. Corrected working source `experiments/icosahedral-phasewindow-20261022/SHORTTUBE.md` has Git blob SHA1 `fb196df953768138c6dd6290c46307e83a988487`, local SHA-256 `0dd3487b016e70f1e1910be7a3dbb84518e222fb4690c3749df201372132751a`. New immutable `shorttube-004` captures this corrected proof and erratum, plus unchanged executable source and output. This is a mathematical notation correction, **not** a new independent science result or a retuned model.
