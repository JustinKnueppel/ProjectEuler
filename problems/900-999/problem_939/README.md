# Problem 939

[Link](https://projecteuler.net/problem=939)

Two players A and B are playing a variant of Nim.  
At the beginning, there are several piles of stones. Each pile is either at the side of A or at the side of B. The piles are unordered.

They make moves in turn. At a player's turn, the player can

*   either choose a pile on the opponent's side and remove one stone from that pile;
*   or choose a pile on their own side and remove the whole pile.

The winner is the player who removes the last stone.

Let $E(N)$ be the number of initial settings with at most $N$ stones such that, whoever plays first, A always has a winning strategy.

For example $E(4) = 9$; the settings are: 

| 1 | $4$       | none   |
| 2 | $1, 3$    | none   |
| 3 | $2, 2$    | none   |
| 4 | $1, 1, 2$ | none   |
| 5 | $3$       | $1$    |
| 6 | $1, 2$    | $1$    |
| 7 | $2$       | $1, 1$ |
| 8 | $3$       | none   |
| 9 | $2$       | none   |

Find $E(5000) \\bmod 1234567891$.
