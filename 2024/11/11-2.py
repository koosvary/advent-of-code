import functools
import time

blinks = 75

@functools.cache
def doStoneyThings(stone, times):
    if times == 0:
        return 1

    if stone == 0:
        return doStoneyThings(1, times - 1)
    elif len(str(stone)) % 2 == 0:
        stone = str(stone)
        midpoint = int(len(stone) / 2)
        return doStoneyThings(int(stone[:midpoint]), times - 1) + doStoneyThings(int(stone[midpoint:]), times - 1)
    else:
        return doStoneyThings(stone * 2024, times - 1)

with open("2024/11/input.txt") as f: 
    for line in f:
        stones = line.split()
        stones = list(map(int, stones))

        total = 0;
        for stone in stones:
            total += doStoneyThings(stone, blinks)
        print(total)
