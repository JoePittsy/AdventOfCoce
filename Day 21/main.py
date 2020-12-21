#!/usr/bin/python3
# Joseph Pitts 20th of December 2020
from collections import defaultdict
import networkx as nx
from networkx.algorithms.bipartite import hopcroft_karp_matching


def read_data(path):
    dataset = []
    with open(path) as f:
        for line in f.readlines():
            tmp = []
            line = line.split("(")
            tmp.append(line[0].strip().split())
            tmp.append(line[1].strip()[9:-1].split(", "))
            dataset.append(tmp)
    return dataset


def task_one(dataset):
    allergens = defaultdict(list)
    for ingredients, allergens_in_ingredients in dataset:
        for allergen in allergens_in_ingredients:
            allergens[allergen].append(ingredients)

    for name, possibles in allergens.items():
        suspect_ingredients = set(possibles[0]).intersection(*possibles[1:])
        allergens[name] = suspect_ingredients

    network = []
    for name, ingredients in allergens.items():
        for ingredient in ingredients:
            network.append((name, ingredient))

    allergen_names = allergens.keys()

    network = nx.Graph(network)
    matching = hopcroft_karp_matching(network)

    allergens_part1 = [match[1] for match in matching.items() if match[0] in allergen_names]
    allergens_part2 = [match for match in matching.items() if match[0] in allergen_names]

    all_ingredients = [i for ingredient in dataset for i in ingredient[0]]
    non_allergens = [i for i in all_ingredients if i not in allergens_part1]
    print(",".join([ingredient[1] for ingredient in sorted(allergens_part2, key=lambda x: x[0])]))

    return len(non_allergens)



if __name__ == "__main__":
    data = read_data("input.txt")
    print(f"Answer for Task One is {task_one(data)}")
