"""Solution to problem 260 on project euler"""
# https://projecteuler.net/problem=260

# A game is played with three piles of stones and two players.
At her turn, a player removes one or more stones from the piles. However, if she takes stones from more than one pile, she must remove the same number of stones from each of the selected piles.
# In other words, the player chooses some N>0 and removes:

# A winning configuration is one where the first player can force a win.
For example, (0,0,13), (0,11,11) and (5,5,5) are winning configurations because the first player can immediately remove all stones.
# A losing configuration is one where the second player can force a win, no matter what the first player does. 
For example, (0,1,2) and (1,3,3) are losing configurations: any legal move leaves a winning configuration for the second player.


# Initial issue loading problem, likely graphic on site