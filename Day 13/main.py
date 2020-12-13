#!/usr/bin/python3
# Joseph Pitts 13th of December 2020

from itertools import count


def read_data(path):
    with open(path) as f:
        lines = f.readlines()
        time = int(lines[0].rstrip())
        dataset = lines[1].strip().split(",")

    return time, dataset


def task_one(time, dataset):
    bus_timetable = sorted([int(i) for i in dataset if i != "x"])

    time_waiting = {}

    for bus in bus_timetable:
        # No point starting at 0, by taking the integer
        # remainder we will always be bellow time bu a little
        mutli = time // bus
        sum = 0
        while sum <= time:
            sum = bus * mutli
            mutli += 1
        time_waiting[bus] = sum - time

    # Find the smallest wait
    sort = {k: v for k, v in sorted(time_waiting.items(), key=lambda item: item[1])}
    key = list(sort.keys())[0]
    return key * sort[key]


def task_two(data):
    # Generate array of tuple (index, bus_id)
    data = [(i, int(bus_id)) for i, bus_id in enumerate(data) if bus_id != 'x']
    # First Bus ID
    jump = data[0][1]
    time_stamp = 0
    # For busses after the frist
    for delta, bus_id in data[1:]:
        while (time_stamp + delta) % bus_id != 0:
            time_stamp += jump
        jump *= bus_id
    return time_stamp


if __name__ == "__main__":
    time, dataset = read_data("input.txt")
    print(f"Answer for Task One is {task_one(time, dataset)}")
    print(f"Answer for Task Two is {task_two( dataset)}")
