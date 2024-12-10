from queue import Queue
f = open('day10Input')
a = []
for line in f:
    a.append([int(x) for x in line.strip()])

h = len(a)
w = len(a[0])

score = 0
rating = 0
dirs_x = [0, 0, -1, 1]
dirs_y = [-1, 1, 0, 0]

for i in range(h):
    for j in range(w):
        if a[i][j] == 0:
            q = Queue()
            q.put((i, j))
            ways = {(i, j): 1}
            while not q.empty():
                x, y = q.get()
                if a[x][y] == 9:
                    score += 1
                    rating += ways[(x, y)]
                for dx, dy in zip(dirs_x, dirs_y):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w:
                        if a[nx][ny] == a[x][y] + 1:
                            if (nx, ny) not in ways:
                                ways[(nx, ny)] = 0
                                q.put((nx, ny))
                            ways[(nx, ny)] += ways[(x, y)]

print(score)
print(rating)
