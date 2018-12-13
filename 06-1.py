"""
break up a grid into cells by figuring out the closest point to the cell using Manhattan distance calculation
Find the area of the largest non-infinite cell

Lookups: Manhattan Distance, Voronoi Diagram, Fortune's Algorithm, python's zip function, anonymous functions

Comments: The brute force method was getting tedious with bug fixes so I started researching better solutions. The Voronoi Diagramming you pointed out had a link to Fortune's Algorithm, which sweeps a line across the grid to limit the data space and backfills solved cells. I dont think I'm up for solving parabolas but I think I can use the concept to at least make solving the puzzle more scalable.


"""
TESTING = True
my_input = []
if TESTING:
        my_input = [[1,1],
                    [1,6],
                    [8,3],
                    [3,4],
                    [5,5],
                    [8,9]]

if not TESTING:
    with open('06input.txt') as f:
        for line in f.readlines():
            new_line = line.split(',')
            my_input.append([int(new_line[0]), int(new_line[1])])

my_input = sorted(my_input)
scores = {}
for point in my_input:
    scores[str(point)] = 0
x_max = max(min(zip(*my_input)))
y_max = max(max(zip(*my_input)))
manhattan = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])

def closest_point_check(cell, points):
    #returns a list of coordinates (as strings) which are closest to the cell. 1 means it is completely owned by 1 point
    closest_distance = 10000
    measurements = {}
    for point in points:
        dist = manhattan(cell, point)
        if dist < closest_distance:
            closest_distance = dist
            measurements[str(point)] = dist
    closest_list = []
    for point in measurements:
        if measurements[point] == closest_distance:
            closest_list.append(point)

    return closest_list

for x in range(x_max):
    for y in range(y_max):
        closest = closest_point_check([x,y], my_input)
        if len(closest) == 1:
            scores[closest[0]] += 1
            if x == 0 or x == x_max+1 or y == 0 or y == y_max+1:
                scores[closest[0]] += 10000000

for score in scores:
    if scores[score] < 10000:
        print scores[score]
