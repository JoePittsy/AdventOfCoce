#!/usr/bin/python3
# Joseph Pitts 1st of December 2020

def read_data(path):
    big_nums = []
    small_nums = []
    with open(path, "r") as file:
        for line in file.readlines():
            num = int(line)
            if num < 1000:
                small_nums.append(num)
            else:
                big_nums.append(num)
    return big_nums, small_nums


def task_one(big, small):
    for b_num in big:
        for s_num in small:
            if b_num + s_num == 2020:
                return b_num * s_num


def task_two(small):
    for i, s_num in enumerate(small):
        for j, s_num2 in enumerate(small[i + 1:]):
            for k, s_num3 in enumerate(small[j + 1:]):
                if s_num + s_num2 + s_num3 == 2020:
                    return s_num * s_num2 * s_num3


if __name__ == "__main__":
    big, small = read_data("input.txt")
    print(f"Answer for Task One is {task_one(big, small)}")
    print(f"Answer for Task Two is {task_two(small)}")
