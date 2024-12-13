instructions = [];

allLines = [];
goodLines = [];

sum = 0;

def testInput(num, numsBefore, numsAfter):
    for numBefore in numsBefore:
        if f"{num}|{numBefore}" in instructions:
            return False;

    for numAfter in numsAfter:
        if f"{numAfter}|{num}" in instructions:
            return False;

    return True;


def testLine(line):
    numsBefore = []
    numsAfter = [int(numeric_string) for numeric_string in line.split(',')];
    
    while len(numsAfter) > 0:
        num = numsAfter.pop(0);
        if not testInput(num, numsBefore, numsAfter):
            return False;
        numsBefore.append(num);
    
    return True;

with open('2024/05/input.txt') as f:
    for i, line in enumerate(f):
        line = line.strip();
        if len(line) == 0:
            continue;

        if '|' not in line:
            # it's an input
            allLines.append(line);
        else:
            # it's an instruction
            instructions.append(line);
    
for line in allLines:
    if testLine(line):
        goodLines.append(line)

for line in goodLines:
    nums = [int(numeric_string) for numeric_string in line.split(',')];
    index = int(len(nums) / 2);
    sum += nums[index];

print(sum)