#!/usr/bin/python3
# Joseph Pitts 16th of December 2020

import numpy as np
import networkx as nx
from networkx.algorithms.bipartite import hopcroft_karp_matching


def read_data(path):
    with open(path) as f:
        file_data = f.read()
        file_data = file_data.split("\n\n")
        rules = [rule for rule in file_data[0].split("\n")]
        rules = {keys.split(": ")[0]: [v.split(" or ") for v in keys.split(": ")[1:]] for keys in rules}
        for key in rules.keys():
            ranges = rules[key][0]
            rules[key] = [[int(num) for num in range.split("-")] for range in ranges]
        my_ticket = [int(i) for i in file_data[1].split(":")[1].strip().split(",")]
        nearby_tickets_raw = file_data[2].split(":")[1].split("\n")
        nearby_tickets = []
        for ticket in nearby_tickets_raw[1:]:
            nearby_tickets.append([int(i) for i in ticket.split(",")])

        return rules, my_ticket, nearby_tickets


def task_one(rules, others):
    rule_list = rules.values()

    def check_validity(number):
        for rule in rule_list:
            for sub_rule in rule:
                valid = bool(sub_rule[0] <= number <= sub_rule[1])
                if valid:
                    return True
        return number

    all_invalid = [i for ticket in others for i in list(map(check_validity, ticket)) if i is not True]
    return sum(all_invalid)


def task_two(rules, mine, others):
    rule_list = rules.values()

    def check_validity(number):
        for rule in rule_list:
            for sub_rule in rule:
                valid = bool(sub_rule[0] <= number <= sub_rule[1])
                if valid:
                    return True
        return False

    def check_field_validity(number):
        rule = rules[field_name]
        for sub_rule in rule:
            valid = bool(sub_rule[0] <= number <= sub_rule[1])
            if valid:
                return True
        return False

    all_valid = np.array([ticket for ticket in others if False not in list(map(check_validity, ticket))])

    network = []
    for field_name in rules:
        for column in range(len(all_valid[0])):
            valid = True if False not in list(map(check_field_validity, all_valid[:, column])) else False
            if valid:
                network.append((field_name, column))
    network = nx.Graph(network)
    # Use the Hopcroft Karp bipartite matching algorithm to match the field
    matching = hopcroft_karp_matching(network)
    total = 1

    for key in matching.keys():
        if isinstance(key, str):
            if "departure" in key:
                total *= mine[matching[key]]

    return total


if __name__ == "__main__":
    r, m, o = read_data("input.txt")
    print(f"Answer for Task One is {task_one(r, o)}")
    print(f"Answer for Task Two is {task_two(r, m, o)}")
