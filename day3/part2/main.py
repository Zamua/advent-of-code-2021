from collections import Counter
lines = ol = cl = [line.rstrip() for line in open("in").readlines()]
get_counters = lambda l: list(map(Counter, [[l[row][col] for row in range(len(l))] for col in range(len(l[0]))]))
sort_counts = lambda c: sorted([(count, digit) for digit, count in c.most_common()], reverse=True)
filter_lines = lambda c, cc, fl, i: list(filter(lambda line: line[i] == sort_counts(c[i])[cc][1], fl))

for i in range(len(lines[0])):
    if len(ol) > 1:
        ol = filter_lines(get_counters(ol), 0, ol, i)
    if len(cl) > 1:
        cl = filter_lines(get_counters(cl), -1, cl, i)

print(int("".join(list(ol)[0]), 2)*int("".join(list(cl)[0]), 2))
