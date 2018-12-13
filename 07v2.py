"""
Day 7 looks like a search tree. I need to research how to build one and step through one, ensuring all steps are explored
First identify and build all the nodes
Then build the tree and sort the nodes
Then step through the tree sequence

Lookups: had to refresh knowledge on tree terminology.

Comments: This one was pretty intuitive so it was just a matter of doing a lot
of testing to make sure I was building it right.

Im learning a lot about using the python debugger on this one

My solution gets the test right and the real input wrong. The solution includes a visualization (at the bottom) that looks
solid. Im moving on for now and will come back later.
"""
import string

TESTING = False
my_input = []

class Node:
    def __init__(self, name, my_tree):
        self._name = name
        self.children = []
        self.depth = None
        self.parents = []
        self.work_time = piece_time(self.get_name())
        my_tree.add_node(self)

    def __str__(self):
        return str([self._name, "Parents:", self.parents])

    def add_child(self, child):
        self.children.append(child)
        child.add_parent(self)

    def add_parent(self, parent):
        self.parents.append(parent)

    def set_depth(self, depth):
        self.depth = depth

    def get_name(self):
        return self._name

class Tree:
    def __init__(self):
        self.levels = [] #need to find the max depth to know how many levels to make
        self.all_nodes = []

    def __str__(self):
        my_tree = []
        for node in self.all_nodes:
            my_tree.append(node)
        return str(my_tree)

    def add_node(self, node):
        self.all_nodes.append(node)

    def node_by_name_get(self, node):
        # returns a node or None if we can't find the node by its name
        for my_node in self.all_nodes:
            if my_node.get_name() == node:
                return my_node
        return None

    def organize_tree(self):
        self.all_nodes.sort(key=sort_name)

    def make_sequence(self):
        # list our node names
        unsequenced_nodes = self.all_nodes[:]
        target_length = len(unsequenced_nodes)
        # available node list is empty
        sequence = ''
        node_index = 0
        while len(sequence) < target_length:
            # check the nodes and if it either has no parent or its parents are all already in the sequence, add it to the sequence
            node = unsequenced_nodes[node_index]
            node_name = unsequenced_nodes[node_index].get_name()
            if len(node.parents) == 0:
                sequence += node_name
                unsequenced_nodes.remove(node)
                node_index = 0
                continue
            else:
                all_parents_in = True
                for parent in node.parents:
                    if parent.get_name() not in sequence:
                        all_parents_in = False
                        break
                if all_parents_in:
                    sequence += node.get_name()
                    unsequenced_nodes.remove(node)
                    node_index = 0
                    continue
            node_index += 1
            # repeat until the node list is empty
        return sequence

class Worker:
    def __init__(self):
        self.part = None
        self.part_time = 0

    def _reset(self):
        self.part = None
        self.part_time = 0

    def finish_part(self):
        if self.part_time > 0:
            return "ERROR: Worker Part time > 0"
        finished_part = self.part
        self._reset()
        return finished_part

    def has_part(self):
        return self.part is not None

    def do_work(self):
        global time
        self.part_time -= time
        return self.part_time

    def take_part(self, part):
        self.part = part
        self.part_time = part.work_time


def sort_name(node):
    #used to get a sorted list of children
    return node.get_name()


def piece_time(piece):
    global time
    #returns an int for the time the part takes (step time + index of letter in alphabet + 1 since the set is 1 indexed)
    #expects part as an uppercase letter (plus one)
    letters = string.ascii_uppercase
    return letters.index(piece) + time


def refresh_pile(parts_pile, done_pile):
    # returns a list of parts ready for work, and a new copy of the parts pile
    parts_copy = parts_pile[:]
    ready_parts = []
    # check for the parentage of parts
    for part in parts_pile:
        parents = part.parents
        parents_complete = True
        for parent in parents:
            if parent.get_name() not in done_pile:
                parents_complete = False
        if len(parents) == 0 or parents_complete:
            ready_parts.append(part)
            parts_copy.remove(part)
    return [ready_parts, parts_copy]

tree = Tree()

if TESTING:
    my_input = [
        "Step C must be finished before step A can begin.",
        "Step C must be finished before step F can begin.",
        "Step A must be finished before step B can begin.",
        "Step A must be finished before step D can begin.",
        "Step B must be finished before step E can begin.",
        "Step D must be finished before step E can begin.",
        "Step F must be finished before step E can begin."
    ]
    workers = 2
    time = 1

if not TESTING:
    with open("07input.txt") as f:
        for line in f.readlines():
            my_input.append(line)
    workers = 5
    time = 60

for line in my_input:
    # find the first capital letter and then the 2nd capital letter
    # create 2 nodes and link them (via tree)
    new_line = line.split(' ')
    node1 = new_line[1] # parent node
    node2 = new_line[7] # child node

    child = tree.node_by_name_get(node2)
    parent = tree.node_by_name_get(node1)
    if not parent:
        parent = Node(node1, tree)
    if not child:
        child = Node(node2, tree)
    parent.add_child(child)

tree.organize_tree()

sequence = tree.make_sequence()
print(sequence)

# Given the sequence we can determine piece availability by looking up parents
pieces = [tree.node_by_name_get(letter) for letter in sequence]
total_time = 0
done_pile = ""
active_parts = []
workers_list = [Worker() for i in range(workers)]

### Worker Tests
#new_worker = Worker()
#new_worker.take_part(pieces[0])
#print new_worker.has_part()
#print new_worker.do_work(), new_worker.do_work(), new_worker.do_work()
#print new_worker.finish_part()

while len(done_pile) < len(sequence):
    for worker in workers_list:
        if worker.has_part():
            if worker.do_work() <= 0:
                finished_part = worker.finish_part()
                done_pile += finished_part.get_name()
        else:
            #pile refresh logic and get a part if possible
            refresh = refresh_pile(pieces, done_pile)
            pieces = refresh[1]
            for ready_part in refresh [0]:
                active_parts.append(ready_part)
            #take a part if available, go idle otherwise
            if len(active_parts) > 0:
                worker.take_part(active_parts.pop(0))
                if worker.do_work() <= 0:
                    finished_part = worker.finish_part()
                    done_pile += finished_part.get_name()
            else:
                pass

    total_time += time

    # TEST BLOCK
    my_string = ''
    my_string += str(total_time) + ' '
    for worker in workers_list:
        if worker.has_part():
            my_string += worker.part.get_name() + " "
        else:
            my_string += '. '
    my_string += done_pile
    print my_string

print total_time
print done_pile

"""
60 H P X Y . 
120 . . . . D HPXY
180 L O . . . HPXYD
240 . . T C . HPXYDLO
300 . . . . N HPXYDLOTC
360 G Q S . . HPXYDLOTCN
420 . . . E M HPXYDLOTCNGQS
480 . . . . . HPXYDLOTCNGQSEM
540 I . Z B . HPXYDLOTCNGQSEMA
600 . . . . K HPXYDLOTCNGQSEMAIZB
660 . . . . . HPXYDLOTCNGQSEMAIZBK
720 R . . . . HPXYDLOTCNGQSEMAIZBK
780 . U W . . HPXYDLOTCNGQSEMAIZBKR
840 . . . V . HPXYDLOTCNGQSEMAIZBKRUW
900 . . . . F HPXYDLOTCNGQSEMAIZBKRUWV
960 . . . . . HPXYDLOTCNGQSEMAIZBKRUWVF
1020 J . . . . HPXYDLOTCNGQSEMAIZBKRUWVF
1080 . . . . . HPXYDLOTCNGQSEMAIZBKRUWVFJ
"""