"""
Project Euler problem #20
by Andrew Kobach
Date: 4 Nov 2022

Find the sum of the digits in the number 100!
"""

import math


if __name__ == "__main__":
    # python can do this
    digits = [int(x) for x in str(math.factorial(100))]
    print(sum(digits))