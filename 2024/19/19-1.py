import functools

patterns = set()
combinations = set()

@functools.cache
def testComboIsValid(combo):
    if len(combo) == 0:
        return True

    foundGoodCombo = False
    for pattern in patterns:
        if combo.startswith(pattern):
            remainingCombo = combo.replace(pattern, '', 1)
            foundGoodCombo = foundGoodCombo or testComboIsValid(remainingCombo)
    return foundGoodCombo

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
    if testComboIsValid(combo):
        counter += 1
        
print(counter)
