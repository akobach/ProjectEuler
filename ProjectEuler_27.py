"""
Project Euler problem #2
by Andrew Kobach
Date: 22 Nov 2022

Considering quadratics of the form n^2 + an + b, where |a| and |b| < 1000.
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n = 0.
"""


def is_prime(n):
    if n <= 2:
        return False

    for k in range(3, n // 2 + 1):
        if n % k == 0:
            return False
    return True


def num_primes_generated(a, b):
    for n in range(0, 1000):  # random guess on the max of n
        if not is_prime(n**2 + a*n + b):
            return n - 1
    return None


if __name__ == "__main__":
    largest_num_primes = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            num_primes = num_primes_generated(a, b)
            if num_primes > largest_num_primes:
                largest_num_primes = num_primes
                result = a*b
    print(result)









