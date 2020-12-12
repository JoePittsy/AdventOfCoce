#!/usr/bin/python3
# Joseph Pitts 11th of December 2020

from copy import deepcopy


def pretty_print(s):
    for i in s:
        print("".join(i))
    print()


def read_data(path):
    dataset = []
    with open(path) as f:
        for line in f.readlines():
            dataset.append(list(line.rstrip()))

    return dataset


# def task_one(seatplan):
#     def query(y, x):
#         if y < 0 or x < 0 or y > height - 1 or x > width - 1:
#             return "."
#         return old_seats[y][x]
#
#     width = len(seatplan[0])
#     height = len(seatplan)
#     seats = deepcopy(seatplan)
#     old_seats = deepcopy(seatplan)
#     old_seats_new = deepcopy(seatplan)
#     last = False
#
#     for _ in range(300):
#         for y in range(height):
#             for x in range(width):
#                 old_seats_new[y][x] = seats[y][x]
#
#                 current_seat = query(y, x)
#
#                 neighbours = [
#                     query(y - 1, x - 1),  # Top Left
#                     query(y - 1, x),  # Top
#                     query(y - 1, x + 1),  # Top Right
#                     query(y, x - 1),  # Left
#                     query(y, x + 1),  # Right
#                     query(y + 1, x - 1),  # Bottom Left
#                     query(y + 1, x),  # Bottom
#                     query(y + 1, x + 1),  # Bottom Right
#                 ]
#
#                 if current_seat == "L" and "#" not in neighbours:
#                     seats[y][x] = "#"
#                 elif current_seat == "#" and len(["#" for seat in neighbours if seat == "#"]) >= 4:
#                     seats[y][x] = "L"
#         pretty_print(seats)
#         old_seats = old_seats_new
#
#         # if seats == old_seats_new and last:
#         #
#         # last = seats == old_seats
#         print(len([1 for row in seats for seat in row if seat == "#"]))
#     return len([1 for row in seats for seat in row if seat == "#"])

def task_one(seatplan):
    def query(y, x):
        if y < 0 or x < 0:
            return "."
        try:
            return seats[y][x]
        except IndexError:
            return "."

    width = len(seatplan[0])
    height = len(seatplan)
    seats = []

    while seats != seatplan:
        seats = deepcopy(seatplan)
        for y in range(height):
            for x in range(width):
                current_seat = query(y, x)
                neighbours = [query(y-1, x-1), query(y-1, x), query(y-1, x+1),
                              query(y, x-1),                  query(y, x+1),
                              query(y+1, x-1), query(y+1, x), query(y+1, x+1)]

                occupied = [seat for seat in neighbours if seat == "#"]
                if current_seat == "L" and "#" not in neighbours:
                    seatplan[y][x] = "#"
                elif current_seat == "#" and len(occupied) >= 4:
                    seatplan[y][x] = "L"

    return len([seat for row in seatplan for seat in row if seat == "#"])


def task_two(seatplan):
    def query(y, x):
        if y < 0 or x < 0:
            return "L"
        try:
            return old_seats[y][x]
        except IndexError:
            return "L"

    width = len(seatplan[0])
    height = len(seatplan)
    seats = deepcopy(seatplan)
    old_seats = deepcopy(seatplan)
    old_seats_new = deepcopy(seatplan)
    last = False

    coeffs = [
        [-1, -1], [-1, 0], [-1, +1],
        [0, -1], [0, +1],
        [+1, -1], [+1, 0], [+1, +1]
    ]

    while True:
        for y in range(height):
            for x in range(width):
                old_seats_new[y][x] = seats[y][x]

                current_seat = query(y, x)

                neighbours = [None, None, None,
                              None, None,
                              None, None, None]
                c = 1
                while any(seat is None for seat in neighbours):
                    for i, (a, b) in enumerate(coeffs):
                        seat = query(y - a * c, x - b * c)
                        if neighbours[i] is None and seat != ".":
                            neighbours[i] = seat
                    c += 1

                if current_seat == "L" and "#" not in neighbours:
                    seats[y][x] = "#"
                elif current_seat == "#" and len(["#" for seat in neighbours if seat == "#"]) >= 5:
                    seats[y][x] = "L"

        old_seats = old_seats_new
        if seats == old_seats and last:
            break
        last = seats == old_seats
    return len([1 for row in seats for seat in row if seat == "#"])


if __name__ == "__main__":
    s = read_data("input.txt")
    print(f"Answer for Task One is {task_one(s)}")
    s = read_data("input.txt")
    print(f"Answer for Task Two is {task_two(s)}")
