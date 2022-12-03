import sys
from collections import Counter

file = sys.argv[1] 

def readInput(file):
    with open(file, 'rt') as f:
        rucksacks = f.read().rstrip()
        rucksacks = rucksacks.split("\n")
    return rucksacks


def partOne(rucksacks):
    priority_sum = 0
    for rucksack in rucksacks:
        mid = len(rucksack) // 2
        c1 = Counter(rucksack[:mid])
        c2_duplicates = Counter()
        c2 = rucksack[mid:]
        for item_type in c2: 
            if item_type in c1 and item_type not in c2_duplicates:
                if item_type.isupper():
                    priority_sum += (ord(item_type.lower()) % 96 + 26)
                elif item_type.islower():
                    priority_sum += (ord(item_type) % 96)
            c2_duplicates[item_type] += 1
    return priority_sum

def partTwo(rucksacks):
    priority_sum = 0
    for i in range(0, len(rucksacks), 3):
        first_elf = Counter(rucksacks[i])
        second_elf = Counter(rucksacks[i + 1])
        third_elf = Counter()
        for item_type in rucksacks[i + 2]:
            if item_type not in third_elf:
                if item_type in first_elf and item_type in second_elf:
                    if item_type.isupper():
                        priority_sum += (ord(item_type.lower()) % 96 + 26)
                    elif item_type.islower():
                        priority_sum += (ord(item_type) % 96)
            third_elf[item_type] += 1
    return priority_sum


def test():
    item_type = 't'
    x = ord(item_type.lower()) % 96 + 26
    y = ord(item_type) % 96 
    print(y)

if __name__ == '__main__':
    data = readInput(file)
    p1 = partOne(data)
    p2 = partTwo(data)
    print("Part One:", p1)
    print("Part Two:", p2)
