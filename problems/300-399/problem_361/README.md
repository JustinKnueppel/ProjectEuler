# Problem 361

[Link](https://projecteuler.net/problem=361)

The **Thue-Morse sequence** $\\{T\_n\\}$ is a binary sequence satisfying:

*   $T\_0 = 0$
*   $T\_{2n} = T\_n$
*   $T\_{2n + 1} = 1 - T\_n$

The first several terms of $\\{T\_n\\}$ are given as follows:  
$01101001{\\color{red}10010}1101001011001101001\\cdots$ 

We define $\\{A\_n\\}$ as the sorted sequence of integers such that the binary expression of each element appears as a subsequence in $\\{T\_n\\}$.  
For example, the decimal number $18$ is expressed as $10010$ in binary. $10010$ appears in $\\{T\_n\\}$ ($T\_8$ to $T\_{12}$), so $18$ is an element of $\\{A\_n\\}$.  
The decimal number $14$ is expressed as $1110$ in binary. $1110$ never appears in $\\{T\_n\\}$, so $14$ is not an element of $\\{A\_n\\}$. 

The first several terms of $\\{A\_n\\}$ are given as follows:

| $n$   | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$  | $9$  | $10$ | $11$ | $12$ | $\cdots$ |
| $A_n$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $9$ | $10$ | $11$ | $12$ | $13$ | $18$ | $\cdots$ |

We can also verify that $A\_{100} = 3251$ and $A\_{1000} = 80852364498$. 

Find the last $9$ digits of $\\sum \\limits\_{k = 1}^{18} A\_{10^k}$.