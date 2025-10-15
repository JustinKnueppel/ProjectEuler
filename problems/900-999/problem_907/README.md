# Problem 907

[Link](https://projecteuler.net/problem=907)

An infant's toy consists of $n$ cups, labelled $C\_1,\\dots,C\_n$ in increasing order of size. 

![0907_four_cups.png](resources/images/0907_four_cups.png?1723769212)

The cups may be stacked in various combinations and orientations to form towers. The cups are shaped such that the following means of stacking are possible: 

*   Nesting: $C\_k$ may sit snugly inside $C\_{k+1}$.
    ![0907_nesting.png](resources/images/0907_nesting.png?1723769266)
*   Base-to-base: $C\_{k+2}$ or $C\_{k-2}$ may sit, right-way-up, on top of an up-side-down $C\_k$, with their bottoms fitting together snugly.
    ![0907_base_to_base.png](resources/images/0907_base_to_base.png?1723769276)
*   Rim-to-rim: $C\_{k+2}$ or $C\_{k-2}$ may sit, up-side-down, on top of a right-way-up $C\_k$, with their tops fitting together snugly.
    ![0907_rim_to_rim.png](resources/images/0907_rim_to_rim.png?1723769283)
*   For the purposes of this problem, it is **not** permitted to stack **both** $C\_{k+2}$ and $C\_{k-2}$ rim-to-rim on top of $C\_k$, despite the schematic diagrams appearing to allow it:
    ![0907_rim_to_rim_counter_example.png](resources/images/0907_rim_to_rim_counter_example.png?1740699245)

Define $S(n)$ to be the number of ways to build a single tower using all $n$ cups according to the above rules.  
You are given $S(4)=12$, $S(8)=58$, and $S(20)=5560$. 

Find $S(10^7)$, giving your answer modulo $1\\,000\\,000\\,007$.
