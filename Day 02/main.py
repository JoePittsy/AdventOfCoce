#!/usr/bin/python3
# Joseph Pitts 2nd of December 2020

def read_data(path):
    dataset = []
    with open(path, "r") as file:
        for line in file.readlines():
            tmp = line.rstrip().split(":")
            dataset.append([tmp[0][:-2].split("-"), tmp[0][-2:][1:], tmp[1][1:]])
    return dataset


def task_one(dataset):
    valid_count = 0
    for entry in dataset:
        min_occur = int(entry[0][0])
        max_occur = int(entry[0][1])
        letter = entry[1]
        password = entry[2].replace("", " ")[1: -1]
        # Count expects words so we add a space between each character in the password to make it a 'word'
        occurrences = password.count(letter)
        if min_occur <= occurrences <= max_occur:
            valid_count += 1

    return valid_count


def task_two(dataset):
    valid_count = 0
    for entry in dataset:
        # Minus one because its 1 indexed not zero
        first_index = int(entry[0][0]) - 1
        second_index = int(entry[0][1]) - 1
        letter = entry[1]
        password = entry[2]
        # Convert to bool and do xor
        if bool(password[first_index] == letter) ^ bool(password[second_index] == letter):
            valid_count += 1

    return valid_count


if __name__ == "__main__":
    dataset = read_data("input.txt")
    print(dataset)
    print(f"Answer for Task One is {task_one(dataset)}")
    print(f"Answer for Task Two is {task_two(dataset)}")
