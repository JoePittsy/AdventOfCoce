#!/usr/bin/python3
# Joseph Pitts 12th of December 2020

def read_data(path):
    dataset = []
    with open(path) as f:
        for line in f.readlines():
            tmp = line.rstrip()
            dataset.append((tmp[0], int(tmp[1:])))

    return dataset


def task_one(dirs):
    momentum = {"N": 0, "E": 0, "S": 0, "W": 0}

    compass = ["N", "E", "S", "W"]
    heading = 1
    current_direction = compass[heading]

    for instruction, num in dirs:
        if instruction == "F":
            momentum[current_direction] += num
        elif instruction in ["R", "L"]:
            if instruction == "L":
                num = 360 - num
            heading += (num // 90)
            heading %= 4
            current_direction = compass[heading]
        else:
            momentum[instruction] += num

    return abs(momentum["N"] - momentum["S"]) + abs(momentum["E"] - momentum["W"])


def task_two(dirs):
    wx, wy = 10, 1
    x = y = 0
    compass = {"N": 1, "E": 1, "S": -1, "W": -1}

    for instruction, num in dirs:

        if instruction in ["N", "S"]:
            wy += num * compass[instruction]
        if instruction in ["E", "W"]:
            wx += num * compass[instruction]

        elif instruction == "F":
            x += wx * num
            y += wy * num

        elif instruction in ["R", "L"]:
            # Swap around for every turn of the compass
            for _ in range(num // 90):
                if instruction == "R":
                    wx, wy = wy, -wx
                else:
                    wx, wy = -wy, wx

    return abs(y) + abs(x)


if __name__ == "__main__":
    dirs = read_data("input.txt")
    print(f"Answer for Task One is {task_one(dirs)}")
    print(f"Answer for Task Two is {task_two(dirs)}")
