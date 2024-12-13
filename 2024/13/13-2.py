import re

a1 = a2 = b1 = b2 = c1 = c2 = 0
totalTokensSpent = 0

def nums(string):
    return tuple(int(string) for string in re.findall(r"(\-*\d+)", string))

def doCramersRule():
    # Will he say it?
    det = (a1 * b2) - (a2 * b1)
    detX = (c1 * b2) - (c2 * b1)
    detY = (a1 * c2) - (a2 * c1)

    x = detX / det
    y = detY / det

    return (x, y)

def seeIfSpentTokens():
    global totalTokensSpent
    x, y = doCramersRule()
    if x.is_integer() and y.is_integer():
        tokensSpent = x * 3 + y
        totalTokensSpent += tokensSpent   

with open("2024/13/input.txt") as f:
    for line in f:
        line = line.strip()

        if len(line) == 0:
            seeIfSpentTokens()             
            continue

        line = line.split(':')
        label, input = line[0], line[1]

        match label:
            case "Button A":
                a1, a2 = nums(input)
            case "Button B":
                b1, b2 = nums(input)
            case "Prize":
                c1, c2 = nums(input)
                c1 +=  10_000_000_000_000
                c2 +=  10_000_000_000_000

seeIfSpentTokens()             
print(totalTokensSpent)


        