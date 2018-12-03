"""part 2 uses the same input. I used a similar method to process the input but stored a list of values for lookup
and made the module recursive.
This solution results in a huge number of iterations and took about 3 minutes of processing to succeed
I looked up more elegant solutions and they're more mathy than I can handle without deeper study
"""

def do_math(my_list, freq=0, results=[]):
    frequency = freq
    found_dupe = False

    for line in my_list:
        frequency += int(line)
        if frequency in results:
            return frequency
        else:
            results.append(frequency)
    return do_math(my_list, frequency, results)

#test block
#test = ['-6', '+3', '+8', '+5', '-6']
#print do_math(test)

inputlist = []

with open('01input.txt') as f:
    for line in f.readlines():    #had to look up whether I wanted file.readline or file.readlines()
        inputlist.append(line)

print(do_math(inputlist))

