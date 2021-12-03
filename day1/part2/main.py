import sys
measurements = list(map(int, sys.stdin.readlines()))
print(sum([1 for i, _ in enumerate(measurements, start=4) if sum(measurements[i-4:i-1]) < sum(measurements[i-3:i])]))
