import itertools

idealResult = [];

def applyOperator(left, right, op):
    if op == '0':
        return left + right;
    elif op == '1':
        return left * right;
    elif op == '2':
        return int(str(left) + str(right));
    else:
        raise Exception("bruh");

def testSequence(desiredResult, nums):
    length = len(nums)
    for op in map(''.join, itertools.product('012', repeat=(length-1))):
        calculatedResult = nums[0];
        for i in range(1, length):
            calculatedResult = applyOperator(calculatedResult, nums[i], op[i-1])
            if calculatedResult > desiredResult:
                break;
        if calculatedResult == desiredResult:
            return True;
    return False;
            


with open('2024/07/input.txt') as f:
    total = 0;
    for i, line in enumerate(f):
        split = line.split(':');
        
        idealResult = int(split[0]);

        nums = [int(numeric_string) for numeric_string in split[1].split()];
        if testSequence(idealResult, nums):
            total += idealResult;
    print(total)


