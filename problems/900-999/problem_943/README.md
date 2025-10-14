# Problem 943

[Link](https://projecteuler.net/problem=943)

Given two unequal positive integers $a$ and $b$, we define a self-describing sequence consisting of alternating runs of $a$s and $b$s. The first element is $a$ and the sequence of run lengths is the original sequence.

For $a=2, b=3$, the sequence is: $$2, 2, 3, 3, 2, 2, 2, 3, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 3, 2, 2, 2, 3, 3, 3,...$$ The sequence begins with **two** $2$s and **two** $3$s, then **three** $2$s and **three** $3$s, so the run lengths $2, 2, 3, 3, ...$ are given by the original sequence.

Let $T(a, b, N)$ be the sum of the first $N$ elements of the sequence. You are given $T(2,3,10) = 25$, $T(4,2,10^4) = 30004$, $T(5,8,10^6) = 6499871$.

Find $\\sum T(a, b, 22332223332233)$ for $2 \\le a \\le 223$, $2 \\le b \\le 223$ and $a \\neq b$. Give your answer modulo $2233222333$.