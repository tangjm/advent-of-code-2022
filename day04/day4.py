import sys 
import re

file = sys.argv[1]

def isSubset(x, y):
    """Is x a subset of y?"""
    return y[0] <= x[0] and y[1] >= x[1]

def overlapsWith(x, y):
    return not (x[0] > y[1] or y[0] > x[1])


def readInput(file):
    with open(file, 'rt') as f:
        lines = f.read().rstrip().split('\n')
        pattern = '(\d+)-(\d+),(\d+)-(\d+)'
        pairs = [ re.search(pattern, line).groups() for line in lines ] 
        pairs = [ ([int(x[0]), int(x[1])], [int(x[2]), int(x[3])]) for x in pairs ]
    return pairs


def partOne(pairs):
    return sum([ 1 for pair in pairs if isSubset(pair[0], pair[1]) or isSubset(pair[1], pair[0]) ])


def partTwo(pairs):
    return sum([ 1 for pair in pairs if overlapsWith(pair[0], pair[1]) ])

if __name__ == '__main__':
    data = readInput(file)
    p1 = partOne()
    p2 = partTwo()
    print(p1)
    print(p2)

