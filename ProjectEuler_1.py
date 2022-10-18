"""
Project Euler problem #1
by Andrew Kobach
Date: 17 Oct 2022

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_first_n_ints(k):
    return k*(k+1)/2


def solution(a, b, n):
    ka = (n - (n % a)) / a
    kb = (n - (n % b)) / b
    kab = (n - (n % (a*b))) / (a*b)
    result = int(a*sum_first_n_ints(ka) + b*sum_first_n_ints(kb) - a*b*sum_first_n_ints(kab))
    if n % a == 0 or n % b == 0:
        result -= n
    return result


if __name__ == "__main__":
    a = 3
    b = 5
    n = 1000

    # this solution is analytic
    # only works for two multiples
    print(solution(3, 5, n))