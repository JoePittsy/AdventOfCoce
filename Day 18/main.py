#!/usr/bin/python3
# Joseph Pitts 18th of December 2020

import pyparsing
import re


def read_data(path):
    dataset = []
    with open(path) as f:
        for line in f.readlines():
            dataset.append(line.strip())
    return dataset


def try_int(s):
    try:
        return int(s)
    except ValueError:
        return s


def task_one(data):
    # Match numbers, the Plus and Times symbol and a whitespace
    matcher = pyparsing.Word(pyparsing.alphanums) | '+' | '*' | " "
    # Match them between nested parentheses
    parens = pyparsing.nestedExpr('(', ')', content=matcher)

    def solve(string_equation):
        def _eval(s):
            """
            Evaluates an expression left to right
            :param s: String expresion
            :return: The answer
            """

            total = 0
            operator = None
            list_expr = [i.strip() for i in re.split(r"([\w']+)", s)[1:-1]]

            for i in list_expr:
                item = try_int(i)
                if type(item) is int:
                    if operator == "*":
                        total *= item
                    elif operator == "+":
                        total += item
                    elif operator is None:
                        total = item
                else:
                    operator = item
            return total

        def _solve(list_equation, depth=0):

            memory = []
            simplified_equation = ""

            for index, item in enumerate(list_equation):
                if type(item) != list:
                    memory.append(item)
                else:
                    # Got to a bracket
                    if len(memory) >= 1:
                        memory.pop()
                        simplified_equation += "".join(memory)
                        memory = []
                        new_eq_tmp = f" {list_equation[index - 1]} {_solve(item, depth + 1)}"
                        simplified_equation += new_eq_tmp
                    else:
                        new_eq_tmp = f" + {_solve(item, depth + 1)}"
                        simplified_equation += new_eq_tmp

            simplified_equation = f"{simplified_equation} {''.join(memory)}"
            if index >= len(list_equation) - 1:
                return _eval(simplified_equation)
            return simplified_equation

        groups = parens.parseString("(" + string_equation + ")").asList()[0]
        return _solve(groups)

    ans = sum([solve(question) for question in data])
    return ans


def task_two(data):
    def parenthesise(s):
        return "((" + s.replace("(", "(((").replace(")", ")))").replace("*", "))*((").replace("+", ")+(") + "))"

    return task_one([parenthesise(s) for s in data])


if __name__ == "__main__":
    dataset = read_data("input.txt")
    print(f"Answer for Task One is {task_one(dataset)}")
    print(f"Answer for Task Two is {task_two(dataset)}")
