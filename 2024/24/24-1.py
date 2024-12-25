import functools

codeValues = {}
sequences = {}

def runSequence(code):
    sequence = sequences[code]

    match sequence[1]:
        case 'AND':
            codeValues[code] = getValue(sequence[0]) and getValue(sequence[2])
        case 'OR':
            codeValues[code] = getValue(sequence[0]) or getValue(sequence[2])
        case 'XOR':
            codeValues[code] = getValue(sequence[0]) ^ getValue(sequence[2])

    return codeValues[code]



@functools.cache
def getValue(code):
    if code in codeValues:
        return codeValues[code]
    
    return runSequence(code)


with open('2024/24/input.txt') as f:
    for line in f:
        line = line.strip()

        if '->' in line:
            split = line.split(' -> ')
            result = split[1]
            sequence = tuple(split[0].split(' '))
            sequences[result] = sequence

        elif ':' in line:
            split = line.split(': ')
            code = split[0]
            value = int(split[1])
            codeValues[code] = value

zCodes = []
for code in sequences.keys():
    if code[0] == 'z':
        zCodes.append(code)

zCodes.sort()
print(zCodes)

zValues = ''
for code in reversed(zCodes):
    zValues += str(getValue(code))

print(zValues)
print(int(zValues, 2))