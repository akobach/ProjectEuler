"""
Project Euler problem #3
by Andrew Kobach
Date: 19 Oct 2022

What is the largest prime factor of the number 600851475143 ?
"""



def solution(n):
    # the smallest prime factor is always less than sqrt(n)
    # once the smallest factor is found, divide n by it, and that's the new n
    # whatever n is left after this process is the largest prime factor
    i = 2
    while i < n**0.5 + 1:
        if n % i == 0:
            n = int(n / i)
        i += 1
    return n


if __name__ == "__main__":
    n = 600851475143
    print(solution(n))
