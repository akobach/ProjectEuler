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
