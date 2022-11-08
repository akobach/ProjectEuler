"""
Project Euler problem #21
by Andrew Kobach
Date: 7 Nov 2022

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from prime_sieve import prime_sieve
from itertools import product

SIEVE = prime_sieve(10000)


def d(n):

    # find all prime factors
    prime_factors = []
    n_original = n
    i = 1
    while True:
        if n == 1:
            break

        i += 1
        if not SIEVE[i]:
            continue

        if n % i == 0:
            prime_factors.append(i)
            n = int(n / i)
            i = 1
        else:
            continue

    all_factors = []

    # generate all factors by looping through all possible combinations of prime factors
    for powers in product(range(2), repeat=len(prime_factors)):
        factor = 1
        for p, k in zip(prime_factors, powers):
            factor *= p ** k
        all_factors.append(factor)

    return sum(set(all_factors)) - n_original


if __name__ == "__main__":
    # create set of amicable numbers
    amicable = set()
    max_val = 10_000
    for n in range(2, max_val):
        dn = d(n)

        # skip if d(n) is greater than max_val
        if dn >= max_val:
            continue

        # skip if n and d(n) are not amicable
        if d(dn) != n:
            continue

        # skip if n is equal to d(n)
        if n == dn:
            continue

        # add to set
        amicable.add(n)
        amicable.add(dn)

    print(sum(amicable))
