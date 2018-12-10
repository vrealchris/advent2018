"""
Process a string to crunch out pairs of upper and lowercase letters (same letter) until none remain
Return the length of the final string
Lookups: python String functions

Comments: Try 1 is a recursive algorithm to solve and re-solve the string until it can't be solved anymore.
This is too slow to work on a 50,000 character string

Try 2 is super simple, build a new string, pop the match off the new one if it's a match, append it if not. This is
basically what I originally wanted to do but got lost in the weeds. I lost the track when I realized strings are immutable
Seeing a similar solution online put me back on the path by using the string to build a list, which is mutable.

Part2 was pretty easy with string.replace() There might have been a faster way than iterating through all 26 letters
but it was fast enough for the use case.
"""

import string

TESTING = False

if TESTING: my_string = 'dabAcCaCBAcCcaDA'
# expected result = 'dabCBAcaDA' (Length 10)

if not TESTING:
    with open('05input.txt') as f:
        my_string = f.readline()


def trim_and_crunch(crunch_string, trim_test):
    """
    Scans the string for capital letters and searches left and right of them
    Copies everything left of the scan since the last crunch
    Counts the number of crunches and re-runs scan if the count is 1 or more
    Returns the length of the string if the crunch count is 0
    """
    new_string = ['']
    trimmed_crunch_string = crunch_string.replace(trim_test, '')
    second_trimmed_crunch_string = trimmed_crunch_string.replace(trim_test.swapcase(), '')

    for letter in second_trimmed_crunch_string:
        if new_string[-1] == string.swapcase(letter):
            new_string.pop()
        else:
            new_string.append(letter)
    return new_string[1:]

minimum = 10450
for letter in string.ascii_letters:
    if len(trim_and_crunch(my_string,letter)) < minimum:
        minimum = len(trim_and_crunch(my_string,letter))

print minimum