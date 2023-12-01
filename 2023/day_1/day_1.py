import pandas as pd 

# part I calculation
with open("day_1_input.txt", "r") as file:
    total = 0
    for line in file:
        nums = [c for c in line if c.isdigit()]
        line_total = int(nums[0] + nums[len(nums) - 1])
        total += line_total
    print(f"Part I Solution: {total}")


# part II calculation
num_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def map_nums(s):
    for k, v in num_map.items():
        s = s.replace(k, v)
    return s

def replace_str(s):
    for i in range(len(s)):
        sliced_str = s[:i+1]
        replaced_str = map_nums(sliced_str)
        if replaced_str != sliced_str:  # a replacement was made
            return replace_str(replaced_str + s[i:])  # recurse with the new string
    return s 

with open("day_1_input.txt", "r") as file:
    total = 0
    for line in file:
        line = replace_str(line)
        nums = [c for c in line if c.isdigit()]
        line_total = int(nums[0] + nums[len(nums) - 1])
        total += line_total
    print(f"Part 2 Solution: {total}")