#!/usr/bin/python3
# Joseph Pitts 8th of December 2020

from copy import deepcopy


class Computer:
    def __init__(self, instructions: list):
        self.accumulator = 0
        self.current_operation = 0
        self.instructions = instructions
        self.running = False
        self.ran_instructions = []

    def reset(self, instructions: list):
        self.__init__(instructions)

    def run(self):
        self.running = True

        switch = {"nop": self.nop,
                  "acc": self.acc,
                  "jmp": self.jmp}

        while self.running:
            instruction, number = self.instructions[self.current_operation]
            self.ran_instructions.append(self.current_operation)
            # Call the function
            switch[instruction](number)

            if self.current_operation in self.ran_instructions:
                return False, self.accumulator
            if self.current_operation >= len(self.instructions):
                return True, self.accumulator

    def nop(self, num: int):
        self.current_operation += 1
        return

    def acc(self, num: int):
        self.accumulator += num
        self.current_operation += 1
        return

    def jmp(self, num: int):
        num -= 1
        self.current_operation += num
        self.current_operation += 1
        return


def read_data(path):
    dataset = []
    with open(path, "r") as file:
        for line in file.readlines():
            dataset.append(line.strip().split(" "))
            dataset[-1][1] = int(dataset[-1][1])

    return dataset


def task_one(data):
    handheld = Computer(data)
    return handheld.run()[1]


def task_two(data):
    new_data = deepcopy(data)
    handheld = Computer(data)
    last_index = 0
    # For all the index's of jmp or nop instructions
    for index in [index for index in range(len(data)) if data[index][0] == "jmp" or data[index][0] == "nop"]:
        if last_index != 0:  # Reset the last change
            new_data[last_index][0] = "jmp" if new_data[last_index][0] == "nop" else "nop"

        # Change this instruction
        new_data[index][0] = "jmp" if new_data[index][0] == "nop" else "nop"

        # Rest and re-run
        handheld.reset(new_data)
        success = handheld.run()
        last_index = index

        if success[0]:
            return success[1]


if __name__ == "__main__":
    d = read_data("input.txt")
    print(f"Answer for Task One is {task_one(d)}")
    print(f"Answer for Task Two is {task_two(d)}")