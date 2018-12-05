"""
Requirements: Find the ID of the sheet that has zero overlaps on it
Method: Build the array as before but add a new property in Sheet to track if it's ever overlapping or been overlapped

Comments: I refactored some things to be nicer. I iterate over the list of sheets less frequently by registering each sheet
in the sheet array on creation and getting the max_width and max_height of the sheet grid layout in that first iteration

This also lets me more easily find and operate on a sheet Im not currently operating on so that I can set the
self.overlapping flag in it.
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
    def __init__(self, data, sheet_array):
        self.id = data[2]
        self.left_buffer = data[0][0]
        self.top_buffer = data[0][1]
        self.width = data[1][0]
        self.height = data[1][1]
        self.overlapping = False
        sheet_array.append(self)
        self.array_reference = sheet_array

        self.x_overlap_potential = self.left_buffer + self.width
        self.y_overlap_potential = self.top_buffer + self.height

    def __str__(self):
        return "ID: " + str(self.id) + '\n' + "Left Buffer: " + str(self.left_buffer) + '\n'\
        + "Top Buffer: " + str(self.top_buffer) + '\n'\
        + "Width: " + str(self.width) + '\n' \
        + "Height: " + str(self.height)

    def set_overlapping(self, othersheet_id):
        #this part is a bit confused, since we might enter an infinite loop if I wasnt directly setting the property
        #in the other sheet. If I more properly called a function like this in the other sheet
        self.overlapping = True
        for sheet in self.array_reference:
            if sheet.id == othersheet_id:
                sheet.overlapping = True

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
max_width = 0
max_height = 0

Elf_Sheets = []

for sheet in puzzle_input:
    new_sheet = Sheet(input_parse(sheet), Elf_Sheets)
    if new_sheet.left_buffer + new_sheet.width > max_width:
        max_width = new_sheet.left_buffer + new_sheet.width
    if new_sheet.top_buffer + new_sheet.height > max_height:
        max_height = new_sheet.top_buffer + new_sheet.height

sheet_array = []
#create array of 0s
for x in range(max_width+1):
    row = []
    for y in range(max_height+1):
        row.append([0,0])    #second 0 will be replaced by the ID of the first sheet laying down
    sheet_array.append(row)
# plot each sheet and +1 for each inch of the sheet's dimensions

for sheet in Elf_Sheets:
    for row in range(sheet.height):
        for column in range(sheet.width):
            #print "printing row %s column %s" %(str(sheet.top_buffer+row), str(sheet.left_buffer+column))
            #print "current number in thing " + str(sheet_array[sheet.top_buffer + row][sheet.left_buffer + column])
            sheet_array[sheet.top_buffer + row][sheet.left_buffer + column][0] += 1
            if sheet_array[sheet.top_buffer + row][sheet.left_buffer + column][1] != 0:
                #encode the sheet ID on it
                other_sheet_id = sheet_array[sheet.top_buffer + row][sheet.left_buffer + column][1]
                sheet.set_overlapping(other_sheet_id)
            sheet_array[sheet.top_buffer + row][sheet.left_buffer + column][1] = sheet.id

total_overlapping_square_inches = 0
for row in sheet_array:
    for column in row:
        if column[0] >= 2:
            total_overlapping_square_inches += 1

print total_overlapping_square_inches

non_overlapping_sheet_count = 0
the_one_sheet = 0
for sheet in Elf_Sheets:
    if not sheet.overlapping:
        non_overlapping_sheet_count += 1
        the_one_sheet = sheet.id

if non_overlapping_sheet_count != 1:
    print "non_overlapping_sheet_count should be 1 but is actually " + str(non_overlapping_sheet_count)
print the_one_sheet
