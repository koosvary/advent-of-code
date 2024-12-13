lines = [];
goodLines = 0;

def testLine(line):
    numbers = line.split(' ');

    increasing = bool(int(numbers[0]) < int(numbers[1]))

    for i, number in enumerate(numbers):
        if i == 0:
            continue;

        diff = int(numbers[i]) - int(numbers[i - 1]);

        if increasing and diff < 0:
            return False;

        if not increasing and diff > 0:
            return False;

        if abs(diff) > 3 or diff == 0:
            return False;
    return True;     


with open('2024/02/input.txt') as f:
    for line in f:
        if testLine(line):
            goodLines = goodLines + 1;        
        

print(goodLines);

