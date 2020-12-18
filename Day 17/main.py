#!/usr/bin/python3
# Joseph Pitts 17th of December 2020
from collections import defaultdict
from itertools import product


def read_data(path):
    dataset = []
    with open(path) as f:
        for line in f.readlines():
            tmp = [1 if i == "#" else 0 for i in list(line.strip())]
            dataset.append(tmp)

    return dataset


def task_one(initial_state):
    activated_cubes = [(i, x, 0) for i, c in enumerate(initial_state) for x in range(len(c)) if c[x] == 1]

    for _ in range(6):
        neighbors = defaultdict(int)

        for x, y, z in activated_cubes:
            for dx, dy, dz in product(range(-1, 2), repeat=3):
                if (dx, dy, dz) != (0, 0, 0):
                    neighbors[(x + dx, y + dy, z + dz)] += 1

        # Add cubes that are currently active if they have 2 or 3 active neighbours
        new_cubes = [cube for cube, count in neighbors.items() if cube in activated_cubes and count in [2, 3]]
        # Add previously inactive cubes if they have 3 active neighbours
        new_cubes += [cube for cube, count in neighbors.items() if cube not in activated_cubes and count == 3]

        activated_cubes = new_cubes
    return len(activated_cubes)


def task_two(initial_state):
    activated_cubes = [(i, x, 0, 0) for i, c in enumerate(initial_state) for x in range(len(c)) if c[x] == 1]

    for _ in range(6):
        neighbors = defaultdict(int)

        for x, y, z, t in activated_cubes:
            for dx, dy, dz, dt in product(range(-1, 2), repeat=4):
                if (dx, dy, dz, dt) != (0, 0, 0, 0):
                    neighbors[(x + dx, y + dy, z + dz, t + dt)] += 1

        # Add cubes that are currently active if they have 2 or 3 active neighbours
        new_cubes = [cube for cube, count in neighbors.items() if cube in activated_cubes and count in [2, 3]]
        # Add previously inactive cubes if they have 3 active neighbours
        new_cubes += [cube for cube, count in neighbors.items() if cube not in activated_cubes and count == 3]

        activated_cubes = new_cubes
    return len(activated_cubes)



if __name__ == "__main__":
    d = read_data("input.txt")
    print(f"Answer for Task One is {task_one(d)}")
    print(f"Answer for Task One is {task_two(d)}")
