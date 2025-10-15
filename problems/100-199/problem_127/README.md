# Problem 127

[Link](https://projecteuler.net/problem=127)

The radical of $n$, $\\operatorname{rad}(n)$, is the product of distinct prime factors of $n$. For example, $504 = 2^3 \\times 3^2 \\times 7$, so $\\operatorname{rad}(504) = 2 \\times 3 \\times 7 = 42$.

We shall define the triplet of positive integers $(a, b, c)$ to be an abc-hit if:

1.  $\\gcd(a, b) = \\gcd(a, c) = \\gcd(b, c) = 1$
2.  $a \\lt b$
3.  $a + b = c$
4.  $\\operatorname{rad}(abc) \\lt c$

For example, $(5, 27, 32)$ is an abc-hit, because:

1.  $\\gcd(5, 27) = \\gcd(5, 32) = \\gcd(27, 32) = 1$
2.  $5 \\lt 27$
3.  $5 + 27 = 32$
4.  $\\operatorname{rad}(4320) = 30 \\lt 32$

It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for $c \\lt 1000$, with $\\sum c = 12523$.

Find $\\sum c$ for $c \\lt 120000$.
