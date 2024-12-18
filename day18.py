import time
from queue import Queue
from time import perf_counter

start_time = time.perf_counter()
grid = []
pos = []
f = open('day18Input')
for line in f:
    elems = line.split(',')
    pos.append((int(elems[1]), int(elems[0])))

h = 213
w = 213
grid = [[0 for _ in range(w)] for _ in range(h)]

for x, y in pos:
    grid[x][y] = 1

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

# part 1
q = Queue()
q.put((0, 0))
dist = {(0, 0): 0}
while not q.empty():
    x, y = q.get()
    d = dist[(x, y)]
    for dx, dy in zip(di, dj):
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != 1 and (nx, ny) not in dist:
            q.put((nx, ny))
            dist[(nx, ny)] = d + 1

#print(dist[(h - 1, w - 1)])
print('part 1 time: ', time.perf_counter() - start_time)

# part 2
region_index = 2
for i in range(h):
    for j in range(w):
        if grid[i][j] >= 1:
            continue
        q = Queue()
        q.put((i, j))
        grid[i][j] = region_index
        while not q.empty():
            x, y = q.get()
            for dx, dy in zip(di, dj):
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 0:
                    q.put((nx, ny))
                    grid[nx][ny] = region_index
        region_index += 1

print('part 2 bfs: ', time.perf_counter() - start_time)

p = [x for x in range(region_index)]
sz = [1 for x in p]

def get_root(x):
    if x == p[x]:
        return x
    r = get_root(p[x])
    p[x] = r
    return r

def union(x, y):
    rx = get_root(x)
    ry = get_root(y)
    if sz[rx] < sz[ry]:
        sz[ry] += sz[rx]
        p[rx] = ry
    else:
        sz[rx] += sz[y]
        p[ry] = rx

for x, y in reversed(pos):
    nei = []
    for dx, dy in zip(di, dj):
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] >= 2:
            nei.append((nx, ny))
    if len(nei) == 0:
        p.append(region_index)
        sz.append(1)
        grid[x][y] = region_index
        region_index += 1
    else:
        grid[x][y] = grid[nei[0][0]][nei[0][1]]
        for nx, ny in nei:
            union(grid[x][y], grid[nx][ny])
    if get_root(grid[0][0]) == get_root(grid[h - 1][w - 1]):
        print(f'{y},{x}')
        break

print(len(set(p)) - 2)
print(time.perf_counter() - start_time)
