"""
Requirements: Return a sum-total square inches of overlapping cloth (this illustrates the wasted cloth)
Method: Im comparing each sheet to each other sheet and seeing how many inches between the two overlap
Lookups: I didnt need to look anything up but the puzzle took me a bit longer to figure out how to parse the info and use it well
I had to be very verbose in code to make sense of things

My first full attempt failed because I didnt have enough data to exclude comparing a sheet to itself, so I refactored
things to include the provided ID of each sheet (I had discarded that before)

My 2nd attempt failed because I didnt just need to avoid testing itself but I needed to also avoid testing A to B and B to A

My 3rd attempt failed and Im not really sure why. Investigating other responses to the puzzle seems to show people
plotting out all the sheets on a huge grid so that they can count up the overlapping inches. Ill sleep on it and see where I end up

As discussed the weakness of this was not accounting for the possibility of 3 overlapping sheets and I dont think there
was a way to rescue the previous method.

Finally got it by mapping out the sheets and counting up the cells that have 2 or more sheets overlapping on them
"""
puzzle_input = []

with open('03input.txt') as f:
    for line in f.readlines():
        puzzle_input.append(line)

def input_parse(data):
    #ugly brute force conversion of the input string to something I can use.
    new_data = data.split(' ')
    new_data = new_data[2][0:-1].split(','), new_data[3].split('x'), int(new_data[0][1:])
    new_data = [int(new_data[0][0]),int(new_data[0][1])],[int(new_data[1][0]),int(new_data[1][1])], new_data[2]
    return new_data

class Sheet:
    def __init__(self, data):
        self.id = data[2]
        self.left_buffer = data[0][0]
        self.top_buffer = data[0][1]
        self.width = data[1][0]
        self.height = data[1][1]

        self.x_overlap_potential = self.left_buffer + self.width
        self.y_overlap_potential = self.top_buffer + self.height

    def __str__(self):
        return "ID: " + str(self.id) + '\n' + "Left Buffer: " + str(self.left_buffer) + '\n'\
        + "Top Buffer: " + str(self.top_buffer) + '\n'\
        + "Width: " + str(self.width) + '\n' \
        + "Height: " + str(self.height)

    def _test_overlap(self, other_sheet):
        #returns true if we test the dimensions of both sheets and find that they overlap in both X and Y (and they are unique)
        x_overlap = False
        y_overlap = False
        if self.left_buffer + self.width > other_sheet.left_buffer:
            x_overlap = True
        if self.top_buffer + self.height > other_sheet.top_buffer:
            y_overlap = True
        if x_overlap and y_overlap:
            return True
        else: return False

    def overlap_squares(self, other_sheet):
        if self._test_overlap(other_sheet):
            x_overlap_dimension = abs((self.left_buffer + self.width) - (other_sheet.left_buffer + other_sheet.width))
            y_overlap_dimension = abs((self.top_buffer + self.height) - (other_sheet.top_buffer + other_sheet.height))
            return x_overlap_dimension * y_overlap_dimension
        else:
            return 0

"""
test_input = ['#1 @ 1,3: 4x4', "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
test_sheets = []
for sheet in test_input:
    test_sheets.append(Sheet(input_parse(sheet)))
test_inches = 0

#find the max dimensions of the array
test_max_width = 0
test_max_height = 0
for sheet in test_sheets:
    if sheet.left_buffer + sheet.width > test_max_width:
        test_max_width = sheet.left_buffer + sheet.width
    if sheet.top_buffer + sheet.height > test_max_height:
        test_max_height = sheet.top_buffer + sheet.height
test_sheet_array = []
#create array of 0s
for x in range(test_max_width):
    row = []
    for y in range(test_max_height):
        row.append(0)
    test_sheet_array.append(row)

# plot each sheet and +1 for each inch of the sheet's dimensions
for sheet in test_sheets:
    for row in range(sheet.height):
        for column in range(sheet.width):
            test_sheet_array[sheet.top_buffer + row][sheet.left_buffer + column] += 1

for row in test_sheet_array:
    for column in row:
        if column >= 2:
            test_inches += 1

#scan the array for the total cells with >= 2




if test_inches != 4:
    print "Total Inches not being calculated correctly: Got " +str(test_inches) + " and needed 4"
"""

#Build a list containing all the sheets, so we can iterate through them
Elf_Sheets = []
for sheet in puzzle_input:
    new_sheet = input_parse(sheet)
    Elf_Sheets.append(Sheet(new_sheet))

#Build an array to track all sheet layouts

max_width = 0
max_height = 0

#get the dimensions
for sheet in Elf_Sheets:
    if sheet.left_buffer + sheet.width > max_width:
        max_width = sheet.left_buffer + sheet.width
    if sheet.top_buffer + sheet.height > max_height:
        max_height = sheet.top_buffer + sheet.height
sheet_array = []

#create array of 0s
for x in range(max_width+1):
    row = []
    for y in range(max_height+1):
        row.append(0)
    sheet_array.append(row)

# plot each sheet and +1 for each inch of the sheet's dimensions

for sheet in Elf_Sheets:
    for row in range(sheet.height):
        for column in range(sheet.width):
            #print "printing row %s column %s" %(str(sheet.top_buffer+row), str(sheet.left_buffer+column))
            sheet_array[sheet.top_buffer + row][sheet.left_buffer + column] += 1

total_overlapping_square_inches = 0
for row in sheet_array:
    for column in row:
        if column >= 2:
            total_overlapping_square_inches += 1

print total_overlapping_square_inches
