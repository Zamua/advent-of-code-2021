import sys
measurements = list(map(int, sys.stdin.readlines()))
print(sum([1 for i, measurement in enumerate(measurements[1:], start=1) if measurements[i-1] < measurement]))
