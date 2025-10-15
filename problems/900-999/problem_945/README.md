# Problem 945

[Link](https://projecteuler.net/problem=945)

We use $x\\oplus y$ for the bitwise XOR of $x$ and $y$.  
Define the XOR-product of $x$ and $y$, denoted by $x \\otimes y$, similar to a long multiplication in base $2$, except that the intermediate results are XORed instead of the usual integer addition.  
For example, $7 \\otimes 3 = 9$, or in base $2$, $111\_2 \\otimes 11\_2 = 1001\_2$: $$\\begin{align\*} \\phantom{\\otimes 111} 111\_2 \\\\ \\otimes \\phantom{1111} 11\_2 \\\\ \\hline \\phantom{\\otimes 111} 111\_2 \\\\ \\oplus \\phantom{11} 111\_2 \\phantom{9} \\\\ \\hline \\phantom{\\otimes 11} 1001\_2 \\\\ \\end{align\*}$$ We consider the equation: $$\\begin{align} (a \\otimes a) \\oplus (2 \\otimes a \\otimes b) \\oplus (b \\otimes b) = c \\otimes c \\end{align}$$ 

For example, $(a, b, c) = (1, 2, 1)$ is a solution to this equation, and so is $(1, 8, 13)$. 

Let $F(N)$ be the number of solutions to this equation satisfying $0 \\le a \\le b \\le N$. You are given $F(10)=21$. 

Find $F(10^7)$.
