"""
Project Euler problem #9
by Andrew Kobach
Date: 24 Oct 2022

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a*a + b*b = c*c
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def find_divisors(n):
    # only use for small values of n
    divisors = []
    for i in range(1, n+1):
        if n % i != 0:
            continue
        divisors.append(i)
    return divisors

def solution(z):
    divisors = find_divisors(z)
    for k in divisors:
        for m in divisors:
            if 2*m*k not in divisors:
                continue
            n = int((z/k - 2*m**2)/(2*m))
            if n <= 0 or m <= n:
                continue
            return 2*k**3*m*n*(m**4 - n**4)


if __name__ == "__main__":
    # use Euclid's formula to generate Pythagorean triples
    z = 1000
    print(solution(z))