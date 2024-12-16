from collections import defaultdict
from queue import Queue
f = open('day12Input')
a = []
for line in f:
    a.append(line.strip())

h = len(a)
w = len(a[0])

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# part 1

visited = set()
res = 0
for i in range(h):
    for j in range(w):
        if (i, j) not in visited:
            q = Queue()
            q.put((i, j))
            visited.add((i, j))

            curr_area = 1
            inner_per = 0
            while not q.empty():
                x, y = q.get()
                for dx, dy in zip(di, dj):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w and a[nx][ny] == a[x][y]:
                        if (nx, ny) not in visited:
                            visited.add((nx, ny))
                            curr_area += 1
                            q.put((nx, ny))
                        inner_per += 1

            curr_per = 4 * curr_area - inner_per
            res += curr_area * curr_per
#part 2
visited.clear()

def get_right_val(x, y, nx, ny):
    dx, dy =  nx - x, ny - y
    if (dx, dy) == (-1, 0):
        x, y = nx, ny
    elif (dx, dy) == (0, 1):
        x, y = x, y
    if (dx, dy) == (1, 0):
        x, y = x, y - 1
    if (dx, dy) == (0, -1):
        x, y = x - 1, y - 1
    if x not in range(0, h) or y not in range(0, w):
        return '.'
    return x, y

curr_reg_id = 1
reg_id = [[0 for j in range(w)] for i in range(h)]

def solve(i, j, visited):

    area = 1
    visited.add((i, j))

    # bfs to find region and its area
    region = {(i, j)}
    q = Queue()
    q.put((i, j))
    while not q.empty():
        x, y = q.get()
        reg_id[x][y] = curr_reg_id
        for dx, dy in zip(di, dj):
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and a[nx][ny] == a[x][y]:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    region.add((nx, ny))
                    q.put((nx, ny))
                    area += 1

    # walk around the region to find its outer perimeter
    per = 1
    x, y = i, j + 1
    px, py = i, j
    while (x, y) != (i, j):
        dx, dy =  x - px, y - py
        px, py = x, y
        id = list(zip(di, dj)).index((dx, dy))
        prev_id = id - 1
        if prev_id < 0: prev_id += 4
        next_id = (id + 1) % 4
        dirs = [(di[prev_id], dj[prev_id]), (di[id], dj[id]), (di[next_id], dj[next_id])]
        for dir_i, dir in enumerate(dirs):
            nx, ny = x + dir[0], y + dir[1]
            if get_right_val(x, y, nx, ny) in region:
                x, y = nx, ny
                per += dir_i != 1
                break


    return per, area

res2 = 0
outer_per_m = defaultdict(int)
real_per_m = defaultdict(int)
area_m = defaultdict(int)
for i in range(h):
    for j in range(w):
        if (i, j) not in visited:
            per, area = solve(i, j, visited)
            outer_per_m[reg_id[i][j]] = per
            real_per_m[reg_id[i][j]] = per
            area_m[reg_id[i][j]] = area
            curr_reg_id += 1

# cache neighbour regions of each region
nei = defaultdict(set)
for x in range(h):
    for y in range(w):
        for dx, dy in zip(di, dj):
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if reg_id[x][y] != reg_id[nx][ny]:
                    nei[reg_id[x][y]].add(reg_id[nx][ny])
            else:
                nei[reg_id[x][y]].add(-1)

# for each inner region (i.e. completely within another region, i.e neigbour_count == 1)
# add its outer perimeter to the outer region's real perimeter
while True:
    min_nei_id, min_nei_count = -1, 10000
    for k, v in nei.items():
        if len(v) < min_nei_count:
            min_nei_id, min_nei_count = k, len(v)
    if min_nei_count > 1:
        break
    nei_outer_id = next(iter(nei[min_nei_id]))
    if nei_outer_id != -1:
        real_per_m[nei_outer_id] += outer_per_m[min_nei_id]
        nei[nei_outer_id].remove(min_nei_id)
    del nei[min_nei_id]

for reg in range(1, curr_reg_id):
    res2 += area_m[reg] * real_per_m[reg]
    print(f'reg {reg} area {area_m[reg]} per {real_per_m[reg]}')

print(res)
print(res2)
