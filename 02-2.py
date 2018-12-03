""" String comparison, have to compare a string to a list of strings and find one pair
Requirements: Return the pair that has all but one letter (in the same position in both strings) the same

Lookups: None

"""

my_input = []

#process the input file into a list
with open('02input.txt') as f:
    for line in f.readlines():
        my_input.append(line[0:-1]) #eliminate unnecessary /n in the strings



#compare a string to all of the strings in my_input. If we get a match, return the pair
def string_compare(string1, string2):
    #Returns True if the string matches except for ONE character in the same position in both strings
    one_mismatch = False
    position = 0
    for i in string1:
        if i == string2[position]:
            pass
        else:
            if one_mismatch is False:
                one_mismatch = True
            else:
                return False
        position += 1
    return True

def parse_matching_strings(string1, string2):
    new_string = ''
    position = 0
    for letter in string1:
        if letter == string2[position]:
            new_string += letter
        position += 1
    return new_string

#test
#my_input = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz]"]

for id1 in my_input:
    for id2 in my_input:
        if id1 == id2:
            pass
        elif string_compare(id1, id2):
            print parse_matching_strings(id1, id2)


#answer is the letters that were common between those in the pair