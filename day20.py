from queue import Queue
import time
st = time.perf_counter()
f = open('day20Input')
grid = f.read().splitlines()

h, w = len(grid), len(grid[0])

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

ds = [[-1 for _ in r] for r in grid]
de = [[-1 for _ in r] for r in grid]
for i in range(h):
    for j in range(w):
        ch = grid[i][j]
        d = None
        if ch == 'S':
            sx, sy = i, j
            d = ds
        if ch == 'E':
            ex, ey = i, j
            d = de
        if d is None:
            continue
        d[i][j] = 0
        q = Queue()
        q.put((i, j))
        while not q.empty():
            x, y = q.get()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and d[nx][ny] == -1:
                    if grid[nx][ny] != '#':
                        q.put((nx, ny))
                        d[nx][ny] = d[x][y] + 1
print(h, w)
res = 0
res2 = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] != '#':
            for dx in range(-20, 21):
                for dy in range(-20, 21):
                    dist = abs(dx) + abs(dy)
                    if dist > 20:
                        continue
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < h and 0 <= ny < w and de[nx][ny] != -1:
                        if ds[ex][ey] - (ds[i][j] + dist + de[nx][ny]) >= 100:
                            res2 += 1
                            if dist <= 2:
                                res += 1

print(res)
print(res2)
print('time ', time.perf_counter() - st)


