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
        self.test_history = []

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
        if self.id == other_sheet.id or self.id in other_sheet.test_history:
            return 0
        if self._test_overlap(other_sheet):
            x_overlap_dimension = abs((self.left_buffer + self.width) - (other_sheet.left_buffer + other_sheet.width))
            y_overlap_dimension = abs((self.top_buffer + self.height) - (other_sheet.top_buffer + other_sheet.height))
            self.test_history.append(other_sheet.id)
            return x_overlap_dimension * y_overlap_dimension
        else:
            return 0

"""
test_input = ['#1 @ 1,3: 4x4', "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
sheet_test1 = Sheet(input_parse(test_input[0]))
sheet_test2 = Sheet(input_parse(test_input[1]))
sheet_test3 = Sheet(input_parse(test_input[2]))
print sheet_test1.overlap_squares(sheet_test2) == 4  #tests that the class is properly detecting the overlap squares
print sheet_test2.overlap_squares(sheet_test3) == 0  #tests that non-overlapping sheets return 0
test_inches = 0
for sheet1 in (sheet_test1, sheet_test2, sheet_test3):
    for sheet2 in (sheet_test1, sheet_test2, sheet_test3):
        test_inches += sheet1.overlap_squares(sheet2)
print sheet_test1.test_history

if test_inches != 4:
    print "Total Inches not being calculated correctly: Got " +str(test_inches) + " and needed 4"
"""

#Build a list containing all the sheets, so we can iterate through them

Elf_Sheets = []
for sheet in puzzle_input:
    new_sheet = input_parse(sheet)
    Elf_Sheets.append(Sheet(new_sheet))

total_overlapping_square_inches = 0

for sheet in Elf_Sheets:
    for sheet2 in Elf_Sheets:
        total_overlapping_square_inches += sheet.overlap_squares(sheet2)

print total_overlapping_square_inches