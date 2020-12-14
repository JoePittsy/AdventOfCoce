#!/usr/bin/python3
# Joseph Pitts 14th of December 2020


from itertools import product


def read_data(path):
    dataset = []

    with open(path) as f:
        for line in f.readlines():
            tmp = line.strip().split(" = ")
            if tmp[0] == "mask":
                dataset.append(["mask", list(tmp[1])])
            else:
                mem_address = int(tmp[0][tmp[0].index("[") + 1: -1])
                dataset.append([mem_address, int(tmp[1])])
    return dataset


def task_one(instructions):
    memory = {}
    current_mask = ["X" for _ in range(36)]

    for current_instruction, data in instructions:
        if current_instruction == "mask":
            current_mask = data
        else:
            binary = list(format(data, "036b"))
            for index, char in enumerate(current_mask):
                if char != "X":
                    binary[index] = char

            memory[current_instruction] = int("".join(binary), 2)

    return sum(memory.values())


def task_two(instructions):
    memory = {}
    current_mask = ["X" for _ in range(36)]

    for current_instruction, data in instructions:
        if current_instruction == "mask":
            current_mask = data
        else:
            # Turn the memory address into binary
            binary = list(format(current_instruction, "036b"))
            for index, char in enumerate(current_mask):
                if char != "0":
                    binary[index] = char
            adr = binary

            # Create all permutations for the floating bits
            addresses = []
            x_amount = adr.count("X")
            indices = [index for index, x in enumerate(adr) if x == "X"]
            for combo in product("01", repeat=x_amount):
                new_adr = adr
                for index, c in enumerate(combo):
                    new_adr[indices[index]] = c
                addresses.append(int("".join(new_adr), 2))

            for address in addresses:
                memory[address] = data

    return sum(memory.values())


if __name__ == "__main__":
    i = read_data("input.txt")
    print(f"Answer for Task One is {task_one(i)}")
    print(f"Answer for Task One is {task_two(i)}")
