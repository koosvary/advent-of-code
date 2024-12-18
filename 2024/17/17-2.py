originalRegisters = {}
registers = {}
operands = []

pointer = 0
outs = []

def getComboOperandValue(operand):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4 | 5 | 6:
            return registers[chr(operand + 61)] # 65 is 'A' in ASCII
        case _:
            # 7 is 'reserved'
            raise Exception('bruh')
             
def runOperand(opcode, operand = None):
    global pointer
    pointer += 2

    match opcode:
        case 0:
            #adv
            registers['A'] = int(registers['A']/(2**getComboOperandValue(operand)))
        case 1:
            #bxl
            registers['B'] = registers['B'] ^ operand
        case 2:
            #bst
            registers['B'] = getComboOperandValue(operand) % 8
        case 3:
            #jnz
            if registers['A'] == 0:
                return
            pointer = operand
        case 4:
            #bxc
            registers['B'] = registers['B'] ^ registers['C']
        case 5:
            #out
            outs.append(getComboOperandValue(operand) % 8)
        case 6:
            #bdv
            registers['B'] = int(registers['A']/(2**getComboOperandValue(operand)))
        case 7:
            #cdv
            registers['C'] = int(registers['A']/(2**getComboOperandValue(operand)))

with open('2024/17/input.txt') as f: 
    for i, line in enumerate(f):
        line = line.strip()

        if i == 3:
            continue

        split = line.split(': ')
        if i == 4:
            operands = [int(x) for x in split[1].split(',')]
            break
        
        registers[split[0][-1]] = int(split[1])

print(registers)
print(operands)

originalRegisters = registers.copy()

def isSubarrayAtEnd(arr, sub):
    # Check if the subarray is identical to the end of the array
    return arr[-len(sub):] == sub

patternMatches = [0]
numberFound = False

while not numberFound:
    currentMatch = patternMatches[0]
    valueBin = format(currentMatch, 'o')
    for i in range(8):
        testValue = int(str(valueBin) + str(i), 8)
        
        registers['A'] = testValue
        while pointer < len(operands):
            runOperand(operands[pointer], operands[pointer+1])

        if isSubarrayAtEnd(operands, outs):
            patternMatches.append(testValue)
            print(f'{testValue}: {valueBin} {outs}')

        if outs == operands:
            print(f'Your lucky number is: {testValue}')
            print(','.join(str(out) for out in outs))
            numberFound = True
            break

        registers = originalRegisters.copy()
        outs = []
        pointer = 0
        testValue += 1
    del patternMatches[0]