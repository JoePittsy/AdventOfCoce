#!/usr/bin/python3
# Joseph Pitts 15th of December 2020


def tasks(numbers, limit):
    memory = {num: [index + 1] for index, num in enumerate(numbers)}
    turn = len(numbers)
    last_spoken = numbers[-1]
    memory[last_spoken] = [None]
    # for _ in range(10):
    while turn < limit:
        turn += 1
        # Faster than memory.get()
        try:
            age = memory[last_spoken]
        except KeyError:
            age = [None]

        if age[0] is None:
            memory[last_spoken] = [turn - 1]
            age = 0
        else:
            age.append(turn - 1)
            if len(age) >= 3:
                age = age[1:]
            memory[last_spoken] = age
            age = age[1] - age[0]

        last_spoken = age

    return last_spoken


if __name__ == "__main__":
    dataset = [14, 8, 16, 0, 1, 17]
    print(f"Answer for Task One is {tasks(dataset, 2020)}")
    print(f"Answer for Task Two is {tasks(dataset, 30000000)}")
