"""
Returns the total area of the coordinate with the most spaces around it that are closest to only it

Lookups: wtf is Manhattan Distance?

Comments: Try 1: build a list of possible coordinates and use that to make a dictionary with [coordinate]: closest point
for each grid coord, then I can sum up the coordinate with the most matching closest point
"""
my_input = [[1, 1],
            [1, 6],
            [8, 3],
            [3, 4],
            [5, 5],
            [8, 9]]

def compare_cells(cell1, cell2):
    return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

max_width = 0
max_height = 0

for i in my_input:
    if i[0] > max_height:
        max_height = i[0]
    if i[1] > max_width:
        max_width = i[1]

all_cells = []
for x in range(0, max_height):
    for y in range(0, max_width):
        all_cells.append([x,y])

calculated_cells = {}

for cell1 in all_cells:  # Needs work, not calculating right
    min_distance = 100000
    cell_id = 0
    for cell2 in my_input:
        cell_id += 1
        distance = compare_cells(cell1, cell2)
        if distance < min_distance:
            min_distance = distance
            calculated_cells[str(cell1)] = cell_id
        elif distance == min_distance:
            calculated_cells[str(cell1)] = None
            break
print calculated_cells
for i in range(len(my_input)):
    total = 0
    for thing in calculated_cells.values():
        if thing == i:
            total += 1
    print i, total