"""
Project Euler problem #6
by Andrew Kobach
Date: 22 Oct 2022

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

if __name__ == "__main__":
    # analytic answer
    n = 100
    square_of_sum = (n*(n+1)/2)**2
    sum_of_squares = n*(n+1)*(2*n+1)/6
    result = int(square_of_sum - sum_of_squares)
    print(result)