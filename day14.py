f = open('day14Input')
from queue import Queue
h = 103
w = 101

pos, vel = [], []
for line in f:
    line = line[2:].split(" v=")
    left = line[0].strip().split(",")
    right = line[1].strip().split(",")
    pos.append((int(left[1]), int(left[0])))
    vel.append((int(right[1]), int(right[0])))

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

def printAfter(t, p=False):
    m = [[0 for _ in range(w)] for _ in range(h)]
    #res = [0] * 4
    for p, v in zip(pos, vel):
        q = [p[0] + v[0] * t, p[1] + v[1] * t]
        q[0] %= h
        q[1] %= w
        a = q[0]
        b = q[1]
        m[a][b] = 1
        '''
        if q[0] < h // 2:
            if q[1] < w // 2:
                res[0] += 1
            elif q[1] > w // 2:
                res[1] += 1
        elif q[0] > h // 2:
            if q[1] < w // 2:
                res[2] += 1
            elif q[1] > w // 2:
                res[3] += 1
        '''
    q = Queue()
    islands = 0
    visited = set()
    for i in range(h):
        for j in range(w):
            if m[i][j] == 1 and (i, j) not in visited:
                q.put((i, j))
                visited.add((i, j))
                islands += 1
                while not q.empty():
                    x, y = q.get()
                    for dx, dy in zip(di, dj):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and m[nx][ny] == 1:
                            if (nx, ny) not in visited:
                                visited.add((nx, ny))
                                q.put((nx, ny))
    if p:
        for i in range(h):
            for j in range(w):
                print('.' if m[i][j] == 0 else 'O', end='')
            print()

    return islands

print(printAfter(7847, True))
'''
isl = [0] * 100001
for i in range(1000, 10000+2):
    isl[i] = printAfter(i, False)
    #print(isl[i], end = ' ')
    if isl[i] < 200:
        found = True
        print('found < 100 at', i)
        break
    if i % 100 == 0:
        print('i=', i)
'''


'''
print(res)
r = 1
for x in res:
    r *= x
print(r)
'''
