instructions = [];

allLines = [];
goodLines = [];
badLines = [];

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

def fixLine(line):
    allNums = [int(numeric_string) for numeric_string in line.split(',')];

    length = len(allNums)

    # bubble sort and flip the order of neighbours if they have flipped instructions
    for _ in range(length - 1):
        swapped = False;
        for i in range(len(allNums) - 1):
            if f"{allNums[i+1]}|{allNums[i]}" in instructions:
                swapped = True;
                allNums[i], allNums[i+1] = allNums[i+1], allNums[i];
        length = length - 1;
        if not swapped:
            break;

    return allNums;

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
    if not testLine(line):
        badLines.append(line);

for line in badLines:
    nums = fixLine(line);
    index = int(len(nums) / 2);
    sum += nums[index];

print(sum)