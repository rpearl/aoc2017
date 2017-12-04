import sys

def checksum1(row):
    return max(row) - min(row)
def checksum2(row):
    for mod in row:
        for el in row:
            if el != mod and el % mod == 0:
                return el / mod

s = 0
for line in sys.stdin:
    row = [int(col) for col in line.split()]
    print row
    s += checksum2(row)

print s
