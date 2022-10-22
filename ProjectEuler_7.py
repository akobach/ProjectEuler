"""
Project Euler problem #7
by Andrew Kobach
Date: 22 Oct 2022

What is the 10001st prime number?
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
    # create a large enough sieve of Eratosthenes
    n = int(2e5)

    cnt = 0
    search = 10001
    for i, v in enumerate(prime_sieve(n)):
        if v:
            cnt += 1
        if cnt == search:
            print(i)
            exit()




