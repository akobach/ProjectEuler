"""
Project Euler problem #5
by Andrew Kobach
Date: 21 Oct 2022

What is the smallest positive number that is by all of the numbers from 1 to 20?
"""

# list of all primes less than 20
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]


def list_diff(list1, list2):
    # return a list of the elements of list1 that are not contained in list2
    # elements of a list that have the same value are considered distinct
    l1 = list1.copy()
    l2 = list2.copy()
    for k in list1:
        if k in l2:
            l1.remove(k)
            l2.remove(k)
    return l1


def factors(n):
    # returns list of the prime factorization of n <= 20
    if n > 20:
        print("ERROR: you asked to factor a number larger than 20")
        exit()

    facs = []
    while n > 1:
        for i in PRIMES:
            if n % i == 0:
                facs.append(i)
                n = int(n / i)
    return facs


def solution():
    bucket = []
    for i in range(2, 21):
        bucket += list_diff(factors(i), bucket)

    # multiply all elements in bucket
    result = 1
    for i in bucket:
        result *= i
    return result



if __name__ == "__main__":
    # create a factor bucket
    print(solution())
