import sys
directions = [(line.split()[0], int(line.split()[1])) for line in sys.stdin.readlines()]

aim = 0
horizontal = 0
depth = 0
for d, n in directions:
    if "forward" in d:
        horizontal +=n
        depth += aim*n
    if "down" in d:
        aim += n
    if "up" in d:
        aim -= n

print(horizontal*depth)
