# Binary counting and coordinate shifting of a curve in space 

Given N samples of a curve in space $\vec{X}$ , created by a single array of complex number $Z_n$

$$n=[0,1,2,3,4,...,N]$$
$$\omega=e^{\frac{2\pi i}{T_o}}$$


$$\vec{X}_n=(u_n,v_n,w_n)$$

$$Z_n=r_n\omega^n$$
$$\overline{Z_n}=r_n\omega^{-n}$$


$$u_n=\frac{1}{2}(Z_n+\overline{Z_n})$$


$$v_n=\frac{1}{2i}(Z_n-\overline{Z_n})$$

$$w_n=\frac{log(|Z_n|)}{log(2)}$$


$$s_n=\frac{v_n}{u_n}$$

$$Z_n=u_n+iv_n$$
$$\overline{Z_n}=u_n-iv_n$$



So from a simple complex number array $Z_n$, we can construct 8 curves in space , given by the $2^{dim}$ symmetries in the positive $w$ direction

| Binary | Decimal | MSb | LSb Symmetry | $k_w$| $k_v$| $k_u$ |
|--------|---------|-----|--------------|------|------|-------|
| 000    | 0       | 0   | $u_n+ iv_n$  | 1 | 1 | 1 |
| 001    | 1       | 0   | $u_n- iv_n$  | 1 |  1| -1 | 
| 010    | 2       | 0   | $-u_n+ iv_n$ | 1 | -1|  1 |
| 011    | 3       | 0   | $-u_n- iv_n$ | 1 | -1| -1 |
| 100    | 4       | 1   | $v_n +iu_n$  | 1 | $s_n$ | $\frac{1}{s_n}$ |
| 101    | 5       | 1   | $v_n -iu_n$  | 1 | $s_n$ | -$\frac{1}{s_n}$ |
| 110    | 6       | 1   | $-v_n +iu_n$ | 1 | -$s_n$| $\frac{1}{s_n}$ |
| 111    | 7       | 1   | $-v_n -iu_n$ | 1 | -$s_n$| -$\frac{1}{s_n}$ |