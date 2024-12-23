from collections import Counter
import functools

pairs = set()
trips = set()

def findPossibleHistorianConnections():
    possibleConnections = 0
    for triplet in trips:
        for connection in triplet:
            firstChar = connection[0]
            if firstChar == 't':
                possibleConnections += 1
                break

    return possibleConnections
        
@functools.cache
def maybeAddTriplet(newTriplet):
    trips.add(newTriplet)

@functools.cache
def interconnected(connections):
    first, second, third = connections
    rules = [(first, second) in pairs or (second, first) in pairs,
             (first, third) in pairs or (third, first) in pairs,
             (second, third) in pairs or (third, second) in pairs]
             
    return True if all(rules) else False


def makeAllPossibleConnections(pair):
    first, second = pair

    for otherPair in pairs:
        if Counter(pair) == Counter(otherPair):
            continue

        otherFirst, otherSecond = otherPair
        
        if otherFirst in [first, second]:
            connections = (first, second, otherSecond)
            connectionsSorted = tuple(sorted(connections))
            if interconnected(connectionsSorted):
                maybeAddTriplet(connectionsSorted)
        elif otherSecond in [first, second]:
            connections = (first, second, otherFirst)
            connectionsSorted = tuple(sorted(connections))
            if interconnected(connectionsSorted):
                maybeAddTriplet(connectionsSorted)


    

with open('2024/23/input.txt') as f:
    for line in f:
        line = line.strip()

        pairs.add(tuple(line.split('-')))

    print(pairs)
    print(len(pairs))
    for i, pair in enumerate(pairs):
        makeAllPossibleConnections(pair)

    print(len(trips))

    print(findPossibleHistorianConnections())
    