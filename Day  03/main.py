#!/usr/bin/python3
# Joseph Pitts 3rd of December 2020
from copy import deepcopy


def read_data(path):
    forest = []
    with open(path, "r") as file:
        for line in file.readlines():
            forest.append(line)
    return forest


def task_one(dataset):
    tree_count = 0
    tree_height = len(dataset) - 1
    tree_width = len(dataset[0]) - 1
    pos = [3, 1]
    for _ in range(tree_height):
        if dataset[pos[1]][pos[0]] == "#":
            tree_count += 1
        pos[0] += 3
        pos[1] += 1
        pos[0] %= tree_width

    return tree_count


def task_two(dataset):
    paths = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    total = 1
    for path in paths:
        tree_count = 0
        tree_height = len(dataset) - 1
        tree_width = len(dataset[0]) - 1
        pos = deepcopy(path)
        for _ in range(tree_height // pos[1]):
            if dataset[pos[1]][pos[0]] == "#":
                tree_count += 1
            pos[0] += path[0]
            pos[1] += path[1]
            pos[0] %= tree_width

        total *= tree_count

    return total


if __name__ == "__main__":
    dataset = read_data("input.txt")
    print(f"Answer for Task One is {task_one(dataset)}")
    print(f"Answer for Task Two is {task_two(dataset)}")
