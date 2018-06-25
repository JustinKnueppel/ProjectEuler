"""Solution to problem 338 on project euler"""
# https://projecteuler.net/problem=338

# A rectangular sheet of grid paper with integer dimensions w × h is given. Its grid spacing is 1.
When we cut the sheet along the grid lines into two pieces and rearrange those pieces without overlap, we can make new rectangles with different dimensions.
# For example, from a sheet with dimensions 9 × 4 , we can make rectangles with dimensions 18 × 2, 12 × 3 and 6 × 6 by cutting and rearranging as below:
# Similarly, from a sheet with dimensions 9 × 8 , we can make rectangles with dimensions 18 × 4 and 12 × 6 .
# For a pair w and h, let F(w,h) be the number of distinct rectangles that can be made from a sheet with dimensions w × h .
For example, F(2,1) = 0, F(2,2) = 1, F(9,4) = 3 and F(9,8) = 2. 
Note that rectangles congruent to the initial one are not counted in F(w,h).
Note also that rectangles with dimensions w × h and dimensions h × w are not considered distinct.


# Initial issue loading problem, likely graphic on site