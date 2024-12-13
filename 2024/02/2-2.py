lines = [];
goodLines = 0;

def testTwoNumbers(increasing, first, second):
    diff = int(second) - int(first);
    if increasing and diff < 0:
        return False;

    if not increasing and diff > 0:
        return False;

    if abs(diff) > 3 or diff == 0:
        return False;
    return True;


def testLine(numbers, savedOnce):
    increasing = bool(int(numbers[0]) < int(numbers[1]));

    for i, number in enumerate(numbers):
        if i == 0:
            continue;

        if not testTwoNumbers(increasing, numbers[i - 1], numbers[i]):
            if not savedOnce:
                for j, _ in enumerate(numbers):
                    newArray = numbers[:];
                    newArray.pop(j);
                    if testLine(newArray, True):
                        return True;
                return False;
            else:
                return False;
    return True;     


with open('2024/02/input.txt') as f:
    for line in f:
        line = line.replace('\n','')
        numbers = line.split(' ')
        if testLine(numbers, False):
            goodLines = goodLines + 1;        
        
print(goodLines);