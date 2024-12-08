a = []
with open('day6Input') as f:
    for line in f:
        a.append([x for x in line.strip()])

h = len(a)
w = len(a[0])
print(h,w)
sI = 0
sJ = 0
for i in range(h):
    for j in range(w):
        if a[i][j] == '^':
            sI, sJ = i, j

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
di = 0
i = sI
j = sJ
while True:
    a[i][j] = 'X'
    nI = i + dirs[di][0]
    nJ = j + dirs[di][1]

    if nI < 0 or nI >= h or nJ < 0 or nJ >= w:
        break

    if a[nI][nJ] == '#':
        di = (di + 1) % 4
        continue

    i, j = nI, nJ

ans = 0
ans2 = 0
for i in range(h):
    #print()
    for j in range(w):
        #print(a[i][j], end='')
        if a[i][j] == 'X':
            ans += 1
            if i != sI or j != sJ:
                a[i][j] = '#'

                # check for loop
                ii = sI
                jj = sJ
                di = 0
                s = set()
                loop = False
                while True:
                    if (ii, jj, di) in s:
                        loop = True
                        break
                    s.add((ii, jj, di))
                    nI = ii + dirs[di][0]
                    nJ = jj + dirs[di][1]

                    if nI < 0 or nI >= h or nJ < 0 or nJ >= w:
                        break

                    if a[nI][nJ] == '#':
                        di = (di + 1) % 4
                        continue

                    ii, jj = nI, nJ
                if loop:
                    ans2 += 1

                a[i][j] = 'X'

print(ans)
print(ans2)
