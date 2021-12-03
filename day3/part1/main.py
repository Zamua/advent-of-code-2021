import sys
from collections import Counter
from functools import reduce
lines = sys.stdin.readlines()
print(reduce(lambda g, e: g*e, map(lambda s: int("".join(s), 2), reduce(lambda n, d: (n[0]+d[0], n[1]+d[1]), [(c.most_common()[0][0], c.most_common()[-1][0]) for c in map(Counter, [[lines[row][col] for row in range(len(lines))] for col in range(len(lines[0]))])]))))
