"""
Find the number of the guard who sleeps the most hours * the minute they're most likely to be asleep

Lookups: syntax for dictionary, keep forgetting that. I researched solutions to sorting a list by specific values
and came up with the 'sort_date()' function to give .sort() a key to fully sort the unordered input.

Comments: This one wasnt too tricky, just time consuming to build and test the objects/functions
"""
TESTING = False


class Guard:
    def __init__(self, info, register):
        self.id = get_id_from_line(info)
        self.log = []
        self.minutes_guard_asleep = []
        self.total_sleep_time = 0
        self.most_slept_minute = 0
        self.frequency_of_most_slept_minute = 0
        register.append(self)

    def __str__(self):
        return str(self.id) + '\n' + str(self.log)

    def add_log(self, log_entry):
        self.log.append(log_entry)

    def get_id(self):
        return self.id

    def process_sleep(self):
        # parse the log to set the guard's total sleep time and the minute most slept
        # review the minute and hour of the fell asleep message vs the woke up message if any
        self.current_sleep_minute = None
        self.current_awake_minute = None
        for line in self.log:
            if 'falls asleep' in line[1]:
                self.current_sleep_minute = get_time_from_line(line)[1]
            elif 'wakes up' in line[1]:
                # guard woke up, record the difference and calculate sleep time, add to sleeping minutes
                self.current_awake_minute = get_time_from_line(line)[1]
                self.total_sleep_time += self.current_awake_minute - self.current_sleep_minute
                for i in range(self.current_sleep_minute, self.current_awake_minute):
                    self.minutes_guard_asleep.append(i)
                self.current_sleep_minute = None
                self.current_awake_minute = None
        if len(self.minutes_guard_asleep) > 0:
            self.most_slept_minute = max(set(self.minutes_guard_asleep), key=self.minutes_guard_asleep.count)
            self.frequency_of_most_slept_minute = self.minutes_guard_asleep.count(self.most_slept_minute)
            print(self.most_slept_minute)
            print(self.frequency_of_most_slept_minute)


if TESTING:
    my_input = ["[1518-11-01 00:00] Guard #10 begins shift",
                "[1518-11-01 00:05] falls asleep",
                "[1518-11-01 00:30] falls asleep",
                "[1518-11-01 00:55] wakes up",
                "[1518-11-01 23:58] Guard #99 begins shift",
                "[1518-11-02 00:40] falls asleep",
                "[1518-11-02 00:50] wakes up",
                "[1518-11-03 00:05] Guard #10 begins shift",
                "[1518-11-03 00:24] falls asleep",
                "[1518-11-03 00:29] wakes up",
                "[1518-11-04 00:02] Guard #99 begins shift",
                "[1518-11-04 00:36] falls asleep",
                "[1518-11-04 00:46] wakes up",
                "[1518-11-05 00:03] Guard #99 begins shift",
                "[1518-11-05 00:45] falls asleep",
                "[1518-11-05 00:55] wakes up",
                "[1518-11-01 00:25] wakes up"]

parsed_input = []

if not TESTING:
    with open('04input.txt') as f:
        my_input = f.readlines()


def parse_line(line):
    # returns a list of [[full date as a list],message]
    newline = (line.split(']'))
    year = newline[0][1:].split('-')[0]
    month = newline[0][1:].split('-')[1]
    day = newline[0][1:].split('-')[2][0:2]
    hour = newline[0][-5:-3]
    minute = newline[0][-2:]
    message = newline[1][1:]
    return [[year, month, day, hour, minute], message]


def sort_date(date):
    # returns the date as a tuple so it can be sorted by sort()
    return (date[0][0],date[0][1],date[0][2],date[0][3], date[0][4])


def get_id_from_line(line):
    return int(line[1].split(' ')[1][1:])


def get_time_from_line(line):
    return (int(line[0][3]), int(line[0][4]))


def get_guard_by_id(id, list):
    for guard in list:
        if guard.get_id() == id:
            return guard

# Build parsed_input with useful data in [[date],message] format
for line in my_input:
    parsed_input.append(parse_line(line))
# sort the parsed_input list using the sort_date function to provide the order of messages
parsed_input.sort(key=sort_date)
for line in parsed_input:
    print(line)



# process the parsed list into a set of guards with a constructed sleep/awake history
guards = []
guard_ids = []
current_guard_id = None
current_guard = None
for line in parsed_input:
    if 'begins shift' in line[1]:
        id = get_id_from_line(line)
        if id not in guard_ids:
            new_guard = Guard(line, guards)#make a new guard because we dont know about this one yet
            current_guard = new_guard
            current_guard_id = new_guard.get_id()
            guard_ids.append(id)
        else:
            current_guard_id = id
            current_guard = get_guard_by_id(id, guards)
            get_guard_by_id(id, guards)
    else:
        current_guard.add_log(line)


# PART ONE ANSWER process the guards to get the guard (id) with the most sleeping minutes
max_slept = 0
max_sleeper = None
max_minute = None
max_count_of_most_slept_minute = None
for guard in guards:
    guard.process_sleep()
    if guard.total_sleep_time >= max_slept:
        max_slept = guard.total_sleep_time
        max_sleeper = guard.id
        max_minute = guard.most_slept_minute
print("Part 1 answer = " + str(max_sleeper * max_minute))

# PART TWO ANSWER process the guards to get the ID of the guard who was asleep the most on a given minute
pt2_max_minute_count = 0
pt2_max_sleeper = None
pt2_max_minute = None
for guard in guards:
    guard.process_sleep()
    if guard.frequency_of_most_slept_minute >= pt2_max_minute_count:
        pt2_max_minute = guard.most_slept_minute
        pt2_max_sleeper = guard.id
        pt2_max_minute_count = guard.frequency_of_most_slept_minute

#find the answer
print(pt2_max_sleeper)
print(pt2_max_minute)
for guard in guards:
    if guard.id == 10:
        print(guard.log)

print("Part 2 answer = " + str(pt2_max_sleeper * pt2_max_minute))