# The order matters : Math,Rhythm,Numbers,Monads,Particles,Universe

I saw a post in X  that said:

**"Numbers are particles"**

I immediately thought I agree, without even  understanding clearly the meaning  in the real world of such a statement. Just thought in my infinite ignorance, I agree. That sounds nice. 

That's what I've been thinking about when digressing about monads, trying to understand how just the process of evolving-time could be enough to create geometry and this way creating everything that is observable, expanding from an initial spatial and temporal coordinate and evolving according to  simple set of initial rules. 

Equipped with  great ignorance and electrical-engineer level math I read about Wolphram's ruliad and, most of the time, I feel I understand what he is talking about.Something about "computational-irreducibility" feels really familiar, but I wouldn't be able to articulate a question for him in any meaningful academic context. 

For me Math is the best infinite game available for humans, and I had the "irrational" impulse of start working on a model of a toy-universe where  math is creating everything using the energy and information associated to the beat of a "drum" or the tick of a "clock" at the center of coordinates, what in our game  would be "the center of the universe".

For me, maybe it`s better to  think of a toy-model universe one can model using a set of initial conditions and simple set of rules that ends up describing a set of orbi-curves able to describe some fundamental geometric shapes flexible enough to create everything else, all monads information being  governed by local phenomena and a binary clock at the center of the universe. 

I know this is insanely ambitious for my math level and IQ, and I know how far I am to even make this text understandable.

But I have to insist:

¿How does a mathematician think about designing/describing ad-hoc bridges between binary counting, geometric shapes, monads, vectors and complex numbers?


# About the word Monad and the toy-universe game

We can think of a monad as a virtual particle, that is able to "reflect" or "refract" some information that can be modeled as a color or an associated symbol.

When I think of  monads I think about an apparently-random  set of observable-events that leave as a trace of their occurrence a set of "a-priori-indivisible" entities that have some information associated to them, and this information can be thought as a biased-reflection of their immediate context and the whole system state, but at the same time these entities have their own essence given  by the "universe-architect" at the "beginning", being able to position the monad in context with others, in a specific spatial and temporal coordinate, working as some kind of universe-building-celular-automata governed by the simplest central rules (Central binary clock or "Drum"). 

But using Wikipedia we see some of the real meanings of the word:

* In philosophy: An ultimate atom, or simple, unextended point; something ultimate and indivisible. 

* In functional programming: A data type which represents a specific form of computation, along with the operations "return" and "bind". 

* In category theory: A monoid object in the category of endo-functors of a fixed category. ¿¿¿What???

* Co-monad as  a monad of the opposite category. This makes me think for example "monads" 1 with -1 as the main items in the category positive and negative integers, but also as a sense of direction in space like spin. 


* For context we should mention Leibniz's "La Monadologie" in the sense that 
what is being proposed  can be seen as a modification of occasionalism developed by latter-day Cartesians. 

* Leibniz surmised that there are indefinitely many substances individually 'programmed' to act in a predetermined way, each substance being coordinated with all the others. 

* This is the pre-established harmony which solved the mind-body problem, but at the cost of declaring any interaction between substances a mere appearance.



# The clock at the center of the universe

We can imagine a tick of a clock in the center of the toy-universe, that is there from the beginning. Each tick is transmitted to the whole universe through 
a  wave that travels "instantaneously" everywhere bringing motion to everything that is being built since the "Big Drum Celular Automata Process" started. 


## Why binary counting

We can imagine each monad in the system as being created and transformed by every tick of the clock. This can be thought as some kind of universal digital circuit, where a main clock syncs everything with everything else. In this toy-universe-game the idea is to allow this central clock to provide a geometry where "reality" is displayed. 

# Binary counting and coordinate shifting of a curve in space 

Given N samples of a curve in space $\vec{X}$ , created by a single array of complex number $Z_n$



$$n=[0,1,2,3,4,...,N]$$
$$\omega=e^{\frac{2\pi i}{T_o}}$$
$$\Omega_o=\frac{2\pi }{T_o}$$

$$\vec{X}_n=(u_n,v_n,w_n)$$

$$Z_n=r_n\omega^n$$
$$\overline{Z_n}=r_n\omega^{-n}$$


$$u_n=\frac{1}{2}(Z_n+\overline{Z_n})=r_n cos[\Omega_o n]$$


$$v_n=\frac{1}{2i}(Z_n-\overline{Z_n})=r_n sin[\Omega_o n]$$

$$w_n=\frac{log(|Z_n|)}{log(2)}$$


$$R_n=\frac{v_n}{u_n}$$

$$Z_n=u_n+iv_n$$
$$\overline{Z_n}=u_n-iv_n$$



So from a simple complex number array $Z_n$, we can construct 8 curves in space , given by the $2^{3}$ symmetries in the positive $w$ direction

$$\vec{X_n}=(k_u u_n,k_v v_n,k_w w_n)$$

* xyz x4

| Binary | Decimal | Curve| LSb Symmetry | $k_u$| $k_v$| $k_w$ |
|--------|---------|-----|--------------|------|------|-------|
| 000    | 0       | A   | $u_n+ iv_n$  | 1 | 1 | 1 |
| 001    | 1       | B   | $u_n- iv_n$  | 1 | -1| 1 | 
| 010    | 2       | C   | $-u_n+ iv_n$ | -1 | 1| 1 |
| 011    | 3       | D   | $-u_n- iv_n$ | -1 |- 1| 1 |




* yxz x4
$R_n$

$\frac{1}{R_n}$
| Binary | Decimal | Curve| LSb Symmetry | $k_u$| $k_v$| $k_w$ |
|--------|---------|-----|--------------|------|------|-------|
| 100    | 4       | E   | $v_n +iu_n$  | $R_n$    |  $\frac{1}{R_n}$ |  1 |
| 101    | 5       | F   | $v_n -iu_n$  | $R_n$    |  -$\frac{1}{R_n}$ |  1 |
| 110    | 6       | G   | $-v_n +iu_n$ | -$R_n$    |  $\frac{1}{R_n}$ |  1 |
| 111    | 7       | H   | $-v_n -iu_n$ | -$R_n$    |  -$\frac{1}{R_n}$ |  1 | 


We could continue this table for $k_w=-1$, with the mirrored curves totaling  $2^4$ mirrored curves


Using (x,y,z) as coordinates for simplicity we can see:

$$x=u$$
$$y=v$$
$$z=w$$

This change is just to indicate more clearly that up to 48 curves can be created mirroring the same $\vec{X}$, being the first 8 paths:



$$\vec{X_n}=(k_u u_n,k_v v_n,k_w w_n)$$

For example an array describing a set of curves we will call "Flower" uses 8 mirrored arrays :

* xyz x4

$$\vec{A_n}=\vec{X_n}=(u_n,v_n,w_n)$$
$$\vec{B_n}=(u_n,-v_n,w_n)$$
$$\vec{C_n}=(-u_n,v_n,w_n)$$
$$\vec{D_n}=(-u_n,-v_n,w_n)$$

* yxz x4

$$\vec{E_n}=(v_n,u_n,w_n)$$
$$\vec{F_n}=(v_n,-u_n,w_n)$$
$$\vec{G_n}=(-v_n,u_n,w_n)$$
$$\vec{H_n}=(-v_n,-u_n,w_n)$$


## Other arrays describing  mirrored set of curves

Following the previous logic, we can imagine:

"Wormhole Flower" using 16 Mirrored curves :
* xyz x4
* yxz x4
* xy(-z) x4
* yx(-z) x4

"Atom" structure uses 6*8=48 curves using all possible basic-combinations:

F_0
* xyz x4
* yxz x4

F_1
* xy(-z) x4
* yx(-z) x4

F_2
* zxy x4
* zyx x4

F_3
* (-z)xy x4
* (-z)yx x4

F_4
* xzy x4
* yzx x4

F_5
* x(-z)y x4
* y(-z)x x4



  



