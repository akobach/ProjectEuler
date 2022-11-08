"""
Project Euler problem #22
by Andrew Kobach
Date: 8 Nov 2022

Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position
in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import string


ALPHABET = list(string.ascii_uppercase)


def word_score(s):
    score = 0
    for x in s:
        score += ALPHABET.index(x) + 1
    return score


if __name__ == "__main__":
    with open("names.txt", "r") as f:
        names_list = sorted(f.read().replace('"', "").split(","))

        result = 0
        for i, name in enumerate(names_list):
            result += (i + 1) * word_score(name)

    print(result)
