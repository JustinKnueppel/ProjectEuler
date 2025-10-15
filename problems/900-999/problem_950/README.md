# Problem 950

[Link](https://projecteuler.net/problem=950)

A band of pirates has come into a hoard of treasure, and must decide how to distribute it amongst themselves. The treasure consists of identical, indivisible gold coins.

According to pirate law, the distribution of treasure must proceed as follows:

1.  The most senior pirate proposes a distribution of the coins.
2.  All pirates, including the most senior, vote on whether to accept the distribution.
3.  If at least half of the pirates vote to accept, the distribution stands.
4.  Otherwise, the most senior pirate must walk the plank, and the process resumes from step 1 with the next most senior pirate proposing another distribution.

The *happiness* of a pirate is equal to $-\\infty$ if he doesn't survive; otherwise, it is equal to $c + p\\cdot w$, where $c$ is the number of coins that pirate receives in the distribution, $w$ is the total number of pirates who were made to walk the plank, and $p$ is the *bloodthirstiness* of the pirate.

The pirates have a number of characteristics:

*   Greed: to maximise their happiness.
*   Ruthlessness: incapable of cooperation, making promises or maintaining any kind of reputation.
*   Shrewdness: perfectly rational and logical.

Consider the happiness $c(n,C,p) + p\\cdot w(n,C,p)$ of the most senior surviving pirate in the situation where $n$ pirates, all with equal bloodthirstiness $p$, have found $C$ coins. For example, $c(5,5,\\frac{1}{10}) = 3$ and $w(5,5,\\frac{1}{10})=0$ because it can be shown that if the most senior pirate proposes a distribution of $3,0,1,0,1$ coins to the pirates (in decreasing order of seniority), the three pirates receiving coins will all vote to accept. On the other hand, $c(5,1,\\frac{1}{10}) = 0$ and $w(5,1,\\frac{1}{10}) = 1$: the most senior pirate cannot survive with any proposal, and then the second most senior pirate must give the only coin to another pirate in order to survive.

Define $\\displaystyle T(N,C,p) = \\sum\_{n=1}^N \\left ( c(n,C,p) + w(n,C,p) \\right )$. You are given that $T(30,3,\\frac{1}{\\sqrt{3}}) = 190$, $T(50,3,\\frac{1}{\\sqrt{31}}) = 385$, and $T(10^3, 101, \\frac{1}{\\sqrt{101}}) = 142427$.

Find $\\displaystyle \\sum\_{k=1}^6 T(10^{16},10^k+1,\\tfrac{1}{\\sqrt{10^k+1}})$. Give the last 9 digits as your answer.
