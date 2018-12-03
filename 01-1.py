""" Day 01, reading a list from a file and do math on it
Lookups, reminder for syntax of file.read() vs file.readline() vs file.readlines()
"""

def do_math(my_list):
    frequency = 0
    for line in my_list:
        frequency += int(line)
    return frequency

#test block
#test = ['-10 ', '+20', '+2']
#print do_math(test)

inputlist = []

with open('01input.txt') as f:
    for line in f.readlines():    #had to look up whether I wanted file.readline or file.readlines
        inputlist.append(line)

print(do_math(inputlist))