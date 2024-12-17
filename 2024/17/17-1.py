
registers = {}
operands = []

outs = []

pointer = 0

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

while pointer < len(operands):
    runOperand(operands[pointer], operands[pointer+1])
print(registers)

print(','.join(str(out) for out in outs))