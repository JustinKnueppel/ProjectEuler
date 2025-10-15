# Problem 949

[Link](https://projecteuler.net/problem=949)

Left and Right play a game with a number of words, each consisting of L's and R's, alternating turns. On Left's turn, **for each word**, Left can remove any number of letters (possibly zero), but not all the letters, from the left side of the word. However, at least one letter must be removed from at least one word. Right does the same on Right's turn except that Right removes letters from the right side of each word. The game continues until each word is reduced to a single letter. If there are more L's than R's remaining then Left wins; otherwise if there are more R's than L's then Right wins. In this problem we only consider games with an odd number of words, thus making ties impossible.

Let $G(n, k)$ be the number of ways of choosing $k$ words of length $n$, for which Right has a winning strategy when Left plays first. Different orderings of the same set of words are to be counted separately.

It can be seen that $G(2, 3)=14$ due to the following solutions (and their reorderings): $$\\begin{align} (\\texttt{LL},\\texttt{RR},\\texttt{RR})&:3\\text{ orderings}\\\\ (\\texttt{LR},\\texttt{LR},\\texttt{LR})&:1\\text{ ordering}\\\\ (\\texttt{LR},\\texttt{LR},\\texttt{RR})&:3\\text{ orderings}\\\\ (\\texttt{LR},\\texttt{RR},\\texttt{RR})&:3\\text{ orderings}\\\\ (\\texttt{RL},\\texttt{RR},\\texttt{RR})&:3\\text{ orderings}\\\\ (\\texttt{RR},\\texttt{RR},\\texttt{RR})&:1\\text{ ordering} \\end{align} $$You are also given $G(4, 3)=496$ and $G(8, 5)=26359197010$.

Find $G(20, 7)$ giving your answer modulo $1001001011$.
