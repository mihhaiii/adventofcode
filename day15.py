
grid = []
moves = ''
f = open('day 15Input')
for line in f:
    if line.strip() == "":
        continue
    if line.startswith('#'):
        grid.append([x for x in line.strip()])
    else:
        moves += line.strip()

init_grid = [[x for x in row] for row in grid]
h, w = len(grid), len(grid[0])
for i in range(h):
    for j in range(w):
        if grid[i][j] == '@':
            px, py = (i, j)

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
chrs = '^>v<'
for move in moves:
    dir = dirs[chrs.index(move)]
    blocked = False
    x, y = px, py
    while True:
        nx, ny = x + dir[0], y + dir[1]
        if grid[nx][ny] == '#':
            blocked = True
            break
        x, y = nx, ny
        if grid[nx][ny] == '.':
            break
    if blocked:
        continue
    grid[x][y] = 'O'
    grid[px][py] = '.'
    px += dir[0]
    py += dir[1]
    grid[px][py] = '@'

res = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == 'O':
            res += i * 100 + j

print(res)



# part 2
grid = []
for i in range(h):
    grid.append([])
    for j in range(w):
        x = init_grid[i][j]
        if x == '.':
            grid[-1] += ['.', '.']
        elif x == '#':
            grid[-1] += ['#', '#']
        elif x == '@':
            grid[-1] += ['@', '.']
            px, py = i, j * 2
        else:
            grid[-1] += ['[', ']']

def pr():
    for r in grid:
        for c in r:
            print(c, end='')
        print()
pr()

from queue import Queue
for move in moves:
    dir = dirs[chrs.index(move)]
    blocked = False
    x, y = px, py
    if dir == (-1, 0) or dir == (1, 0):
        nx, ny = x + dir[0], y + dir[1]
        if grid[nx][ny] == '#':
            continue
        if grid[nx][ny] == '.':
            grid[nx][ny] = '@'
            grid[x][y] = '.'
            px, py = nx, ny
            continue
        q = Queue()
        if grid[nx][ny] == '[':
            q.put((nx, ny))
        else:
            q.put((nx, ny - 1))

        vis = {(nx, ny)}
        all = []
        while not q.empty():
            x, y = q.get()
            all.append((x, y))
            nx, ny = x + dir[0], y + dir[1]
            mx, my = nx, ny + 1
            if grid[nx][ny] == '#' or grid[mx][my] == '#':
                blocked = True
                break
            if grid[nx][ny] == '[' and (nx, ny) not in vis:
                q.put((nx, ny))
                vis.add((nx, ny))
            if grid[mx][my] == '[' and (mx, my) not in vis:
                q.put((mx, my))
                vis.add((mx, my))
            if grid[nx][ny] == ']' and (nx, ny - 1) not in vis:
                q.put((nx, ny - 1))
                vis.add((nx, ny - 1))
        if blocked:
            continue
        for x, y in reversed(all):
            nx, ny = x + dir[0], y + dir[1]
            grid[nx][ny] = grid[x][y]
            grid[x][y] = '.'
            grid[nx][ny + 1] = grid[x][y + 1]
            grid[x][y + 1] = '.'
        grid[px][py] = '.'
        px += dir[0]
        py += dir[1]
        grid[px][py] = '@'
    else:
        all = []
        while True:
            nx, ny = x + dir[0], y + dir[1]
            if grid[nx][ny] == '#':
                blocked = True
                break
            if grid[nx][ny] == '.':
                break
            x, y = nx, ny
            all.append((x, y))
        if blocked:
            continue
        for x, y in reversed(all):
            nx, ny = x + dir[0], y + dir[1]
            grid[nx][ny] = grid[x][y]
            grid[x][y] = '.'
        grid[px][py] = '.'
        px += dir[0]
        py += dir[1]
        grid[px][py] = '@'
    #print("after move ", move)
    #pr()
    #print()

print()
pr()

res2 = 0
for i in range(h):
    for j in range(w*2):
        if grid[i][j] == '[':
            res2 += i * 100 + j

print(res2)
