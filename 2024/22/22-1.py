import math

def mixThenPrune(secretNumber, multiplying, mutator):
    if multiplying:
        newSecretNumber = secretNumber * mutator
    else:
        newSecretNumber = math.floor(secretNumber / mutator)
    
    # mix
    newSecretNumber = secretNumber ^ newSecretNumber

    # prune
    newSecretNumber %= 16777216

    return newSecretNumber

total = 0
with open('2024/22/input.txt') as f:
    for line in f:
        line = line.strip()

        secretNumber = int(line)
        for i in range(2000):
            secretNumber = mixThenPrune(secretNumber, True, 64)
            secretNumber = mixThenPrune(secretNumber, False, 32)
            secretNumber = mixThenPrune(secretNumber, True, 2048)

        total += secretNumber
    
print(total)

