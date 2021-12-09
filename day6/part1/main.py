import heapq
fish = list(map(int,  open("../in").readlines()[0].split(',')))
heapq.heapify(fish)

days = 80
while days > 0:
    min_days = max(1, min(days, fish[0]))
    fish_to_add = []
    for _ in range(len(fish)):
        f = heapq.heappop(fish)
        f -= min_days
        if f == -1:
            fish_to_add += [6, 8]
        else:
            fish_to_add += [f]

    for f in fish_to_add:
        heapq.heappush(fish, f)

    days -= min_days
    print(days, len(fish))

