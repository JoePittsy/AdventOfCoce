#!/usr/bin/python3
# Joseph Pitts 4th of December 2020

def read_data(path):
    passports = []
    passport = ""
    with open(path, "r") as file:
        for line in file.readlines():
            if line.rstrip() != "":
                passport += " " + line.rstrip()
            else:
                tmp = passport.strip().split()
                passports.append({key: value for (key, value) in [x.split(":") for x in tmp]})
                passport = ""
        # No new line at end of input so we manually add the last passport out of the for loop
        tmp = passport.strip().split()
        passports.append({key: value for (key, value) in [x.split(":") for x in tmp]})
        return passports


def task_one(passports):
    valid = 0
    for passport in passports:
        try:
            passport.pop("cid")
        except KeyError:
            pass
        valid += 1 if len(passport.keys()) == 7 else 0
    return valid


def task_two(passports):
    valid = 0
    for passport in passports:
        try:
            passport.pop("cid")
        except KeyError:
            pass
        if len(passport.keys()) != 7:
            # Still need all 7 to be valid
            continue
        else:
            validity = True
            while validity:
                validity = validity and (1920 <= int(passport["byr"]) <= 2002)
                validity = validity and (2010 <= int(passport["iyr"]) <= 2020)
                validity = validity and (2020 <= int(passport["eyr"]) <= 2030)
                validity = validity and (passport["hgt"][-2:] == "in" or passport["hgt"][-2:] == "cm")
                validity = validity and (passport["hcl"][0] == "#" and len(passport["hcl"]) == 7)
                validity = validity and (passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
                validity = validity and (len(passport["pid"]) == 9)

                if passport["hgt"][-2:] == "in":
                    validity = (validity and 59 <= int(passport["hgt"][:-2]) <= 76)
                elif passport["hgt"][-2:] == "cm":
                    validity = (validity and 150 <= int(passport["hgt"][:-2]) <= 193)
                break
            valid += validity
    return valid


if __name__ == "__main__":
    passports = read_data("input.txt")
    print(f"Answer for Task One is {task_one(passports)}")
    print(f"Answer for Task Two is {task_two(passports)}")
