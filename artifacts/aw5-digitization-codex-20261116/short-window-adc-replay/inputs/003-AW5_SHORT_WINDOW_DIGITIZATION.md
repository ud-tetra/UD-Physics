# AW5 short-window exterior-channel digitization

**EXACT_INTERNAL / CONDITIONAL / SYNTHETIC. Physical Promotion = 0.**

The [merged exterior-channel derivation](https://github.com/ud-tetra/UD-Physics/pull/397) gives an undamped normalized gap $\Delta R(s)\ge s^6/280$ on $0<s\le 1$. The chosen checkpoint is $s=1$, with $\delta=1/280$. The degree-six polynomials share $1-(3/2)s^2+(1/2)s^4$ and add $-s^6/15$ and $-s^6/12$, respectively. At $s=1$, the hollow remainder is bounded by $1/210$ and the filled remainder by $1/120$. These follow from the fourth spectral moments $192$ and $336$ divided by $8!$. The fixture samples the adverse ends of those certified intervals, so its synthetic unquantized gap attains $\delta$. This constructs a bound-stress fixture, rather than claiming the true cosine traces attain it.

## Conditional deterministic budget

Use a common observation of the two trials, a uniform ideal quantizer spanning $[-2,2)$, and independent provision of an absolute additive error bound $\epsilon$ on each normalized sample. Require measured hollow minus filled to reach $\delta/2=1/560$. With $b$ bits, worst-case rounding shrinks the gap by at most one code width $4/2^b$, and the two additive errors can shrink it by $2\epsilon$. A sufficient condition is
$$
4/2^b+2\epsilon\le 1/560.
$$
Allocate $\epsilon=1/2240$ per trace, half the total allowance in aggregate. The quantizer must then satisfy $2^b\ge4480$, so 13 bits is the minimum integer depth for this sufficient guarantee at the declared span and allocation. The corresponding unit-reference **peak signal-to-error** ratio is 2240 (approximately 67 dB). This is an absolute bound and amplitude-ratio convention. A hardware RMS-SNR specification alone supplies no deterministic peak-error bound.

The two errors in the fixture are adversarial, with opposite signs. The symmetric quantizer uses nearest-code rounding and checks that the modeled inputs and rounded outputs avoid clipping. The automated replay checks the 12/13-bit guarantee boundary, synthesizes and quantizes the adverse pair at 13 bits and checks its exact observed gap. Failing the 12-bit budget means the declared guarantee is unavailable. Particular 12-bit samples can still resolve the pair.

Timing mismatch, differential gain, preparation errors, nonlinearities and actual ADC performance require separate bounds. The fraction $1/2240$ is an allocation, not a measured noise floor. The bound and synthetic check supply no physical admission result.

## Frozen scorer boundary

The checked-in AW5-ACQUISITION-v1 scorer uses 256 midpoints over a longer native window and a $3/64$ contrast margin. This short-window fixture has a separate one-checkpoint criterion. Its replay constructs a three-trace synthetic packet with 256 checkpoints inside the certified short window and confirms that the frozen scorer rejects the time grid. No change to that scorer, its admission rules, or its threshold is made.

Run the replay from its candidate directory inside a UD-Physics checkout with Python 3. The committed result fixture uses exact rational strings.
