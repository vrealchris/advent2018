""" Scanning a list of IDs to find the checksum of A*B where:
 A = number of IDs with at least 1 letter that appears twice in the ID
 B = number of IDs with at least 1 letter that appears 3 times in the ID
#REQUIREMENTS:
#count the id's that contain exactly 2 of any letter
#count the id's that contain exactly 3 of any letter
#multiply the 2 counts as a checksum and return it

Lookups: Dictionary syntax refresher
"""

my_input = []
my_check = [0, 0]

#process the input file into a list
with open('02input.txt') as f:
    for line in f.readlines():
        my_input.append(line[0:-1]) #eliminate unnecessary /n in the strings

test = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

def scan_id(id):
    """
    Scans the id for letters that appear 2 or 3 times
    Returns a list [0 dupes, 2 dupes, 3 dupes]
    ie: 'bababc' returns [0, 1, 1]
    """
    #makes a dictionary of the unique letters and the counts of each
    my_dict = {}
    for i in id:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    has_matches = False

    result = [0, 0, 0]  # result is a code for matches 0, matches 2, or matches 3
    # review the dictionary and return results
    for letter in my_dict:
        if my_dict.get(letter) == 2:
            result[1] = 1
            has_matches = True
        if my_dict.get(letter) == 3:
            result[2] = 1
            has_matches = True
    if not has_matches:
        result[0] = 1

    return result

def parse_results(result, checksum):
    """
    Increments the appropriate parts of the checksum based on the result being parsed
    """
    if result[0] == 1:
        pass
    if result[1] == 1:
        checksum[0] += 1
    if result[2] == 1:
        checksum[1] += 1
    return checksum

for id in my_input:
    parse_results(scan_id(id), my_check)

print my_check[0] * my_check[1]