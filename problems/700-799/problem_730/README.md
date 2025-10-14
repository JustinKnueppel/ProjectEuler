# Problem 730

[Link](https://projecteuler.net/problem=730)

For a non-negative integer $k$, the triple $(p,q,r)$ of positive integers is called a $k$-shifted Pythagorean triple if $$p^2 + q^2 + k = r^2$$ 

$(p, q, r)$ is said to be primitive if $\\gcd(p, q, r)=1$. 

Let $P\_k(n)$ be the number of primitive $k$-shifted Pythagorean triples such that $1 \\le p \\le q \\le r$ and $p + q + r \\le n$.  
For example, $P\_0(10^4) = 703$ and $P\_{20}(10^4) = 1979$. 

Define $$\\displaystyle S(m,n)=\\sum\_{k=0}^{m}P\_k(n).$$ You are given that $S(10,10^4) = 10956$. 

Find $S(10^2,10^8)$.