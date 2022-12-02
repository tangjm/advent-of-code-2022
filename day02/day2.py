import sys 

file = sys.argv[1]

def read(file):
    with open(file, 'rt') as f: 
        data = f.read().rstrip().split("\n\n")
        records = data[0].split("\n")
        records = [ record.split(' ') for record in records ]
        records = list(map(lambda x : ("ABC".index(x[0]), "XYZ".index(x[1])), records))
    return records

def partOne():
    records = read(file)
    score = [ (pair[1] + 1) + ((((pair[1] - pair[0]) % 3 + 1) % 3) * 3) for pair in records ]
    print(score)

def partTwo():
    records = read(file) 
    score = [ (((((pair[1] - 1) % 3) + pair[0]) % 3) + 1) + (((pair[1] - 1) % 3) * 3) for pair in records ]
    print(score)

if __name__ == '__main__':
    partOne()
    partTwo()

