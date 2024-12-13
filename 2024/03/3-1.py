import re

total = 0;

def findMuls(line):
    pattern = re.findall(r"mul\([0-9]+,[0-9]+\)", line)
    return pattern


with open('2024/03/input.txt') as f:
    for line in f:
        operations = findMuls(line);

        for operation in operations:
            mults = re.findall(r'\d+', operation);
            total += int(mults[0]) * int(mults[1]);

print(total)