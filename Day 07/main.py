#!/usr/bin/python3
# Joseph Pitts 7th of December 2020

from re import sub


def read_data(path):
    bag_map = {}
    with open(path, "r") as file:
        for line in file.readlines():
            outer, inners = line.split(" bags contain")
            inner_array = inners.strip(" .\n").split(",")
            inner_array = [sub("(bags|bag)+", "", s).strip().split(" ", 1) for s in inner_array]
            bag_map[outer] = inner_array
    return bag_map


def can_hold_gold(bags, inner_bags):
    names = [i[1] for i in inner_bags]
    if "shiny gold" in names:
        return True
    elif not (len(names) == 1 and names[0] == "other"):
        total = False
        while not total:
            for _, name in inner_bags:
                total += can_hold_gold(bags, bags[name])
            break
        return total
    return False


def count_sub_bags(bags, prev, inner_bags):
    names = [i[1] for i in inner_bags]
    if len(names) == 1 and names[0] == "other":
        return 1
    else:
        total = 0
        for c, n in inner_bags:
            count = [int(b[0]) for b in bags[prev] if n == b[1]][0]
            more_bags = not (len(bags[n]) == 1 and bags[n][0][1] == "other")
            total += int(count) * more_bags + int(c) * count_sub_bags(bags, n, bags[n])
        return total


def task_one(bags):
    return sum([bool(can_hold_gold(bags, bags[i])) for i in bags])


def task_two(bags):
    return count_sub_bags(bags, "shiny gold", bags["shiny gold"])


if __name__ == "__main__":
    bags = read_data("input.txt")
    print(f"Answer for Task One is {task_one(bags)}")
    print(f"Answer for Task Two is {task_two(bags)}")
