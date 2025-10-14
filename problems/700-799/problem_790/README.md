# Problem 790

[Link](https://projecteuler.net/problem=790)

There is a grid of length and width $50515093$ points. A clock is placed on each grid point. The clocks are all analogue showing a single hour hand initially pointing at $12$.

A sequence $S\_t$ is created where: $$ \\begin{align} S\_0 &= 290797\\\\ S\_t &= S\_{t-1}^2 \\bmod 50515093 &t>0 \\end{align} $$ The four numbers $N\_t = (S\_{4t-4}, S\_{4t-3}, S\_{4t-2}, S\_{4t-1})$ represent a range within the grid, with the first pair of numbers representing the x-bounds and the second pair representing the y-bounds. For example, if $N\_t = (3,9,47,20)$, the range would be $3\\le x\\le 9$ and $20\\le y\\le47$, and would include $196$ clocks.

For each $t$ $(t>0)$, the clocks within the range represented by $N\_t$ are moved to the next hour $12\\rightarrow 1\\rightarrow 2\\rightarrow \\cdots $.

We define $C(t)$ to be the sum of the hours that the clock hands are pointing to after timestep $t$.  
You are given $C(0) = 30621295449583788$, $C(1) = 30613048345941659$, $C(10) = 21808930308198471$ and $C(100) = 16190667393984172$.

Find $C(10^5)$.