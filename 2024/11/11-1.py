blinks = 25
stones = []

def doStoneyThings():
    global stones
    newStones = []
    for stone in stones:
        if stone == 0:
            newStones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone = str(stone)
            midpoint = int(len(stone) / 2)
            left, right = int(stone[:midpoint]), int(stone[midpoint:])
            newStones.append(left)
            newStones.append(right)
        else:
            newVal = stone * 2024
            newStones.append(newVal)
    stones = newStones
    print(stones)

with open("2024/11/testinput.txt") as f: 
    for line in f:
        stones = line.split()
        stones = list(map(int, stones))
        print("Initial arrangement:")
        print(stones)

        for i in range(blinks):
            doStoneyThings()
            print(f"After {i} blinks:")
            print(stones)
            print(len(stones))