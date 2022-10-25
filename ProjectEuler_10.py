"""
Project Euler problem #10
by Andrew Kobach
Date: 25 Oct 2022

Find the sum of all the primes below two million.
"""

import numpy as np

def prime_sieve(n):
    if n < 2:
        print("ERROR! Sieve is too small")
        exit()
    sieve = np.full(n+1, True)
    sieve[0] = False
    sieve[1] = False

    for i in range(len(sieve)):
        if not sieve[i]:
            continue
        for k in range(2, int(n/i)+1):
            sieve[i*k] = False

    return sieve


if __name__ == "__main__":
    n = 2000000
    sieve = prime_sieve(n)
    result = 0
    for i in range(n):
        if sieve[i]:
            result += i
    print(result)