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


# Rather than brute force a solution, I've noticed on paper that there's a consistent pattern:
# zXX are always made up of a XOR b - except for maybe the last one (my z45 is OR but seems okay)
# All XORs should have either xXX or yXX as input, or zXX as output like above
# All ANDs should not lead into XORs
# All ORs should be the output of AND, except for x00/y00
# Appears to be a full adder, not sure if that's necessarily true, just looks it on paper

# Find the gates that don't fulfull the criteria above
badGates = []
for code in sequences:
    gate1, operation, gate2 = sequences[code]

    if operation == 'XOR' and all(prefix not in 'xyz' for prefix in (code[0], gate1[0], gate2[0])):
        badGates.append(code)
    if code[0] == 'z':
        if operation != 'XOR':
            badGates.append(code)
    if operation == 'XOR':        
        if 'x00' not in (gate1, gate2):
            if not (gate1[0] in ['x', 'y'] and gate2[0] in ['x', 'y']):
                gate1Operation = sequences[gate1][1]
                gate2Operation = sequences[gate2][1]

                # if gate1Operation == 'AND':
                #     badGates.append(gate1)
                if gate2Operation == 'AND':
                    badGates.append(gate2)
    if operation == 'OR':
        if 'x00' not in (gate1, gate2):
            gate1Operation = sequences[gate1][1]
            gate2Operation = sequences[gate2][1]

            if gate1Operation == 'XOR':
                badGates.append(gate1)
            elif gate2Operation == 'XOR':
                badGates.append(gate2)

print(','.join(sorted(dict.fromkeys(badGates))[:-1])) #drop zXX's most significant bit