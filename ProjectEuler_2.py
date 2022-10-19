"""
Project Euler problem #2
by Andrew Kobach
Date: 18 Oct 2022

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""

def Fn_generator():
    a = 0
    b = 1
    while True:
        a, b = b, a+b
        yield b

def solution(n):
    result = 0
    for i in Fn_generator():
        if i > n:
            break
        if i % 2 == 0:
            result += i

    return result


if __name__ == "__main__":
    n = 4e6

    # brute force solution with a generator
    print(solution(n))
