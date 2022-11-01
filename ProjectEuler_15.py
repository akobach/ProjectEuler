"""
Project Euler problem #14
by Andrew Kobach
Date: 1 Nov 2022

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import scipy.special

if __name__ == "__main__":
    # analytical solution
    grid_size = 20
    print(int(scipy.special.comb(2*grid_size, grid_size)))
