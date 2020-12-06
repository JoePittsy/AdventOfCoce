#!/usr/bin/python3
# Joseph Pitts 6th of December 2020

from functools import reduce


def read_data(path):
    with open(path, "r") as file:
        data = file.read()
    return [i.split("\n") for i in data.split("\n\n")]


def task_one(questions):
    return sum([len(set("".join(i))) for i in questions])


def task_two(questions):
    return sum([len(reduce(set.intersection, [set(i) for i in group])) for group in questions])


if __name__ == "__main__":
    questions = read_data("input.txt")
    print(f"Answer for Task One is {task_one(questions)}")
    print(f"Answer for Task Two is {task_two(questions)}")
