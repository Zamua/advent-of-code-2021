import sys
from collections import Counter
lines = sys.stdin.readlines()

nums = [(c.most_common()[0][0], c.most_common()[-1][0]) for c in map(Counter, [[lines[row][col] for row in range(len(lines))] for col in range(len(lines[0]))])]
gamma = int("".join([num[0] for num in nums]), 2)
epsilon = int("".join([num[1] for num in nums]), 2)
print(gamma*epsilon)
