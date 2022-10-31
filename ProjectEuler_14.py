"""
Project Euler problem #14
by Andrew Kobach
Date: 31 Oct 2022

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def chain_length(n):
    # returns the chain length for starting number n
    cnt = 0
    while True:
        cnt += 1
        if n == 1:
            break
        elif n % 2 == 0:
            n = int(n/2)
        else:
            n = 3*n + 1
    return cnt


if __name__ == "__main__":
    # brute force
    result = 0
    max_length = 0
    for k in range(2, 1_000_000):
        length = chain_length(k)
        if length > max_length:
            max_length = length
            result = k
    print(result)
