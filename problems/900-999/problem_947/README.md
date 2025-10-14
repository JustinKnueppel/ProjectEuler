# Problem 947

[Link](https://projecteuler.net/problem=947)

The $(a,b,m)$-sequence, where $0 \\leq a,b \\lt m$, is defined as

$\\begin{align\*} g(0)&=a\\\\ g(1)&=b\\\\ g(n)&= \\big(g(n-1) + g(n-2)\\big) \\bmod m \\end{align\*}$ 

All $(a,b,m)$-sequences are periodic with period denoted by $p(a,b,m)$.  
The first few terms of the $(0,1,8)$-sequence are $(0,1,1,2,3,5,0,5,5,2,7,1,0,1,1,2,\\ldots )$ and so $p(0,1,8)=12$.

Let $\\displaystyle s(m)=\\sum\_{a=0}^{m-1}\\sum\_{b=0}^{m-1} p(a,b,m)^2$. For example, $s(3)=513$ and $s(10)=225820$.

Define $\\displaystyle S(M)=\\sum\_{m=1}^{M}s(m)$. You are given, $S(3)=542$ and $S(10)=310897$.

Find $S(10^6)$. Give your answer modulo $999\\,999\\,893$.