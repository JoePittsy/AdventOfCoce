#!/usr/bin/python3
# Joseph Pitts 6th of December 2020

from itertools import combinations


def read_data(path):
    dataset = []
    with open(path, 'r') as f:
        for line in f.readlines():
            dataset.append(int(line))

    return dataset


def task_one(numbers, p_size=25):
    for i, n in enumerate(numbers[p_size:]):
        possibilities = [sum(group) for group in combinations(numbers[i:i + p_size], 2)]
        if n not in possibilities:
            return n


def task_two(numbers, invalid):
    for i in range(len(numbers)):
        for j in range(i+2, len(numbers)):
            if sum(numbers[i:j]) == invalid:
                return min(numbers[i:j]) + max(numbers[i:j])



def golf():
    from itertools import combinations
    d = [int(i) for i in open("input.txt").read().split("\n")]
    print([n for i, n in enumerate(d[25:]) if n not in [sum(g) for g in combinations(d[i:i + 25], 2)]][0])
    print([min(d[i:j]) + max(d[i:j]) for i in range(len(d)) for j in range(i+2, len(d)) if sum(d[i:j]) == 2089807806][0])



if __name__ == "__main__":
    golf()

