"""
Project Euler problem #26
by Andrew Kobach
Date: 13 Nov 2022

A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


def get_cycle(d):
    # note: unit cycle is equal to 10^k = 1 (mod d), for some positive integer k
    k = 0
    while True:
        k += 1
        if (10 ** k - 1) % d == 0:
            return (10 ** k - 1) // d


if __name__ == "__main__":
    longest_cycle = 1
    result = 1
    for d in range(3, 1001, 2):
        if d % 5 == 0:
            continue
        cycle = get_cycle(d)
        if cycle > longest_cycle:
            result, longest_cycle = d, cycle
    print(result)


