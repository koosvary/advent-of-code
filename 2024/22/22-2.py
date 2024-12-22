import math
import ast

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

patternSales = {}
with open('2024/22/input.txt') as f:
    
    for line in f:
        line = line.strip()

        secretNumber = int(line)
        sequence = [secretNumber % 10]
        diffs = []
        testedDiffs = []

        for _ in range(2000):
            secretNumber = mixThenPrune(secretNumber, True, 64)
            secretNumber = mixThenPrune(secretNumber, False, 32)
            secretNumber = mixThenPrune(secretNumber, True, 2048)

            newPrice = secretNumber % 10
            sequence.append(newPrice)
            lastPrice = sequence[-2]
            diffs.append(newPrice - lastPrice)

            if len(diffs) >= 4:
                diffPattern = diffs[-4:]
                key = repr(diffPattern)

                # only add to the total if first instance of each sale pattern with this vendor
                if key in testedDiffs:
                    continue
                
                testedDiffs.append(key)

                if key not in patternSales:
                    patternSales[key] = newPrice
                else:
                    patternSales[key] += newPrice

    bestPatternSales = 0
    bestPattern = ''
    for key in patternSales.keys():
        salesMade = patternSales[key]
        
        if salesMade > bestPatternSales:
            bestPatternSales = salesMade
            bestPattern = key

    print(bestPattern)
    print(bestPatternSales)

