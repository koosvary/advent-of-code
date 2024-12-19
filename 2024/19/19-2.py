import functools

patterns = set()
combinations = set()

@functools.cache
def testComboIsValid(combo):
    if len(combo) == 0:
        return 1

    goodCombosFound = 0
    for pattern in patterns:
        if combo.startswith(pattern):
            remainingCombo = combo.replace(pattern, '', 1)
            goodCombosFound += testComboIsValid(remainingCombo)
    return goodCombosFound

with open('2024/19/input.txt') as f:
    for i, line in enumerate(f):
        line = line.strip()

        if i == 0:
            patterns = set(line.split(', '))
        elif i == 1:
            continue
        else:
            combinations.add(line)


counter = 0
for combo in combinations:
    counter += testComboIsValid(combo)
        
print(counter)