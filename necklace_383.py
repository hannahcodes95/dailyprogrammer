# Imagine a necklace with lettered beads that can slide along the string. In this example, you
# could take the N off NICOLE and slide it around to the other end to make ICOLEN. Do it again to get COLENI, and so on.
# For the purpose of today's challenge, we'll say that the strings "nicole", "icolen", and "coleni" describe the same
# necklace.

# Generally, two strings describe the same necklace if you can remove some number of letters from the beginning of one,
# attach them to the end in their original ordering, and get the other string. Reordering the letters in some other way
# does not, in general, produce a string that describes the same necklace.

# Write a function that returns whether two strings describe the same necklace


def necklace(necklacea, necklaceb):

    necklacea_doubled = necklacea + necklacea

    if len(necklacea) != len(necklaceb):
        return False

    return necklaceb in necklacea_doubled



print(necklace('hannah', 'annahh'))
#

# Optional Bonus 1

# If you have a string of N letters and you move each letter one at a time from the start to the end, you'll eventually
# get back to the string you started with, after N steps.
# Sometimes, you'll see the same string you started with before N'steps. For instance, if you start with "abcabcabc",
# you'll see the same string ("abcabcabc") 3 times over the course of moving a letter 9 times.

# Write a function that returns the number of times you encounter the same starting string if you move each letter in the
# string from the start to the end, one at a time.

import collections

def repeated_necklace(string):

    de = collections.deque(string)
    counter = 0

    for i in range(len(string)):
        de.insert(len(de), string[i])
        de.remove(string[i])
        if ''.join(de) == string:
            counter += 1
        print(de)

    return counter

print(repeated_necklace('hannahhannah'))


