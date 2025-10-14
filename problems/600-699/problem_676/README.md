# Problem 676

[Link](https://projecteuler.net/problem=676)

Let $d(i,b)$ be the **digit sum** of the number $i$ in base $b$. For example $d(9,2)=2$, since $9=1001\_2$. When using different bases, the respective digit sums most of the time deviate from each other, for example $d(9,4)=3 \\ne d(9,2)$. 

However, for some numbers $i$ there will be a match, like $d(17,4)=d(17,2)=2$. Let $ M(n,b\_1,b\_2)$ be the sum of all natural numbers $i \\le n$ for which $d(i,b\_1)=d(i,b\_2)$. For example, $M(10,8,2)=18$, $M(100,8,2)=292$ and $M(10^6,8,2)=19173952$. 

Find $\\displaystyle \\sum\_{k=3}^6 \\sum\_{l=1}^{k-2}M(10^{16},2^k,2^l)$, giving the last $16$ digits as the answer.