"""
Process a string to crunch out pairs of upper and lowercase letters (same letter) until none remain
Return the length of the final string
Lookups:

Comments: Try 1 is a recursive algorithm to solve and re-solve the string until it can't be solved anymore.
This is too slow to work on a 50,000 character string

Try 2 is to use python's string.strip() function. I'll build a set of all of the combinations we're looking for and
just strip them out of the string. Should be faster since there's no comparisons being made within the string
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