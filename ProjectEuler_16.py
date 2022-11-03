"""
Project Euler problem #16
by Andrew Kobach
Date: 2 Nov 2022

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

if __name__ == "__main__":
    # python can do this
    n = 2**1000
    n_digits = [int(x) for x in str(n)]
    print(sum(n_digits))
