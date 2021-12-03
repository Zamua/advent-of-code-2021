import sys
directions = sys.stdin.readlines()
print(sum([int(d.split()[1]) for d in filter(lambda x: "forward" in x, directions)]) 
        * (sum([int(d.split()[1]) for d in filter(lambda x: "down" in x, directions)]) 
            - sum([int(d.split()[1]) for d in filter(lambda x: "up" in x, directions)])))
