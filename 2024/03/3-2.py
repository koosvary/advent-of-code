import re

total = 0;

def findMuls(line):
    pattern = re.findall(r"mul\([0-9]+,[0-9]+\)", line)
    return pattern

with open('2024/03/input.txt') as f:
    for line in f:
        operations = findMuls(line);
        instructions = re.findall(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))", line);

        enabled = True;

        for instruction in instructions:
            match instruction[0]:
                case 'do()':
                    enabled = True;
                case 'don\'t()':
                    enabled = False;
                case _:
                    if enabled:
                        mults = findMuls(instruction[0])
                        total += int(instruction[1]) * int(instruction[2]);

        

print(total)