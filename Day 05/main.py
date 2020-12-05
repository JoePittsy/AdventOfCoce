#!/usr/bin/python3
# Joseph Pitts 5th of December 2020


def read_data(path):
    passes = []
    with open(path, "r") as file:
        for line in file.readlines():
            tmp = line.rstrip()
            passes.append([tmp[0:-3], tmp[-3:]])
    return passes


def bsp(limits):
    return limits[1] - (limits[1] - limits[0]) // 2


def task_one(passes):
    highest = -1
    for row_data, column_data in passes:
        rows = [0, 127]
        cols = [0, 7]

        for instruction in row_data:
            switch = {"B": 0, "F": 1}
            rows[switch[instruction]] = bsp(rows)

        for instruction in column_data:
            switch = {"R": 0, "L": 1}
            cols[switch[instruction]] = bsp(cols)

        seat_id = (rows[0] * 8) + cols[0]
        highest = seat_id if seat_id > highest else highest

    return highest


def task_two(passes):
    seat_ids = []

    for row_data, column_data in passes:
        rows = [0, 127]
        cols = [0, 7]

        for instruction in row_data:
            switch = {"B": 0, "F": 1}
            rows[switch[instruction]] = bsp(rows)

        for instruction in column_data:
            switch = {"R": 0, "L": 1}
            cols[switch[instruction]] = bsp(cols)

        seat_ids.append((rows[0] * 8) + cols[0])

    sorted_seats = sorted(seat_ids)
    all_seats = set(range(sorted_seats[0], sorted_seats[-1]))
    sorted_seats = set(sorted_seats)

    my_seat = all_seats - sorted_seats
    return my_seat.pop()


if __name__ == "__main__":
    passes = read_data("input.txt")
    print(f"Answer for Task One is {task_one(passes)}")
    print(f"Answer for Task Two is {task_two(passes)}")
