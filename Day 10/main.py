#!/usr/bin/python3
# Joseph Pitts 10th of December 2020


def read_data(path):
    dataset = []
    with open(path, "r") as file:
        for line in file.readlines():
            dataset.append(int(line.strip()))

    dataset.append(0)
    dataset.append(max(dataset) + 3)
    dataset = sorted(dataset)

    return dataset


def task_one(adapters):
    # In built device always has a difference of 3
    voltage_jumps = {1: 0, 2: 0, 3: 0}

    prev_voltage = adapters[0]
    for adapter in adapters[1:]:
        voltage_jumps[adapter - prev_voltage] += 1
        prev_voltage = adapter

    return voltage_jumps[1] * voltage_jumps[3]


def task_two(adapters):

    found_paths = {}

    def find_from(x):
        if x == len(adapters) - 1:
            return 1
        if x in found_paths:
            return found_paths[x]

        possibilities = 0

        for j in range(x+1, x+4 if x+4 < len(adapters) else len(adapters)):
            if adapters[j] - adapters[x] <= 3:
                possibilities += find_from(j)

        found_paths[x] = possibilities
        return possibilities

    return find_from(0)


if __name__ == "__main__":
    adapters = read_data("input.txt")
    print(f"Answer for Task One is {task_one(adapters)}")
    print(f"Answer for Task Two is {task_two(adapters)}")



