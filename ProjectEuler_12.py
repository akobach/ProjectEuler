"""
Project Euler problem #12
by Andrew Kobach
Date: 28 Oct 2022

What is the value of the first triangle number to have over five hundred divisors?
"""

from collections import Counter
from prime_sieve import prime_sieve


SIEVE = prime_sieve(int(1e5))


def prime_factors(n):
    i = 2
    factors = []
    while True:
        if n == 1:
            break
        if SIEVE[i] and n % i == 0:
            factors.append(i)
            n = int(n / i)
            i = 2
            continue
        i += 1
        if i > n:
            print("ERROR! Sieve is too small!")
            exit()

    return factors


def number_of_triangle_factors(n):
    factors = []

    # n and n+1 are coprime
    if n % 2 == 0:
        factors += prime_factors(int(n/2))
        factors += prime_factors(n+1)
    else:
        factors += prime_factors(int((n+1) / 2))
        factors += prime_factors(n)

    result = 1
    prime_counter_dict = dict(Counter(factors))

    for val in prime_counter_dict.values():
        result *= val + 1

    return result



if __name__ == "__main__":
    search = 500

    n = 1
    while True:
        if number_of_triangle_factors(n) < search:
            n += 1
            continue
        print(int(n*(n+1)/2))
        break


