"""
Project Euler problem #4
by Andrew Kobach
Date: 20 Oct 2022

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def solution():
    result = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            if i*j <= result:
                continue
            s = str(i*j)
            if s[::-1] == s:
                result = i*j
    return result


if __name__ == "__main__":
    # brute force search
    print(solution())