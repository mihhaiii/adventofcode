a = []
with open('day4Input') as f:
    for line in f:
        a.append([x for x in line.strip()])

print(a)

h = len(a)
w = len(a[0])

dx = [0,0,1,1,1,-1,-1,-1]
dy = [1,-1,0,1,-1,0,1,-1]

ans = 0
for i in range(h):
    for j in range(w):
        for di in range(len(dx)):
            in_bounds = True
            s = ""
            for step in range(4):
                ii = i + step * dx[di]
                jj = j + step * dy[di]
                if ii >= 0 and ii < h and jj >= 0 and jj < w:
                    s += a[ii][jj]
                else:
                    in_bounds = False
                    break
            if in_bounds:
                if s == "XMAS":
                    ans += 1

ans2 = 0
for i in range(1,h-1):
    for j in range(1,w-1):
        a1 = a[i-1][j] + a[i][j] + a[i+1][j]
        a2 = a[i][j-1] + a[i][j] + a[i][j+1]

        a3 = a[i-1][j-1] + a[i][j] + a[i+1][j+1]
        a4 = a[i+1][j-1] + a[i][j] + a[i-1][j+1]



        if a3 in ['MAS', 'SAM']:
            if a4 in ['MAS', 'SAM']:
                ans2 += 1


print(ans)
print(ans2)
