#!/usr/bin/python3
# Joseph Pitts 19th of December 2020

import re


def read_data(path):
    rules, strings = [line.strip() for line in open(path).read().split("\n\n")]
    rules = dict([rule.split(": ") for rule in rules.split("\n")])

    return rules, strings


def task_one(rules, strings):
    def generate(key):
        rule = rules[key]
        return rule[1:-1] if '"' in rule \
            else '(?:' + '|'.join(["".join([generate(sub_rule) for sub_rule in op.split()])
                                   for op in rule.split(" | ")]) + ')'

    new_rule = re.compile(generate('0'))
    return sum([1 for s in strings.split("\n") if new_rule.fullmatch(s) is not None])


def task_two(rules, strings):
    def generate(key):
        rule = rules[key]
        if '"' in rule:
            return rule[1:-1]
        elif key == "8":
            return generate('42') + "+"
        elif key == "11":
            # I had to look at r/adventofcode for this, I had no idea
            # It's actually quite a smart little hack, it matches
            # a and b up to 100 times (To avoid recursion)
            a = generate('42')
            b = generate('31')
            return '(?:' + '|'.join(f"{a}{{{n}}}{b}{{{n}}}" for n in range(1, 100)) + ')'
        else:
            sub = []
            for op in rule.split(" | "):
                nums = op.split()
                sub.append("".join(generate(sub_rule) for sub_rule in nums))
            return '(?:' + '|'.join(sub) + ')'

    new_rule = re.compile(generate('0'))
    return sum([1 for s in strings.split("\n") if new_rule.fullmatch(s) is not None])


if __name__ == "__main__":
    r, s = read_data("input.txt")
    print(f"Answer for Task One is {task_two(r, s)}")
