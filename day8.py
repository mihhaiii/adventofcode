a = []
with open('day8Input') as f:
    for line in f:
        a.append(list(line.strip()))

d = {}
h = len(a)
w = len(a[0])
for i in range(h):
    for j in range(w):
        if a[i][j] != '.':
            if a[i][j] in d:
                d[a[i][j]].append((i, j))
            else:
                d[a[i][j]] = [(i, j)]

s = set()
for k, locations in d.items():
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            x1, y1 = locations[i]
            x2, y2 = locations[j]

            x, y = x1, y1
            while 0 <= x < h and 0 <= y < w:
                s.add((x, y))
                x += x1 - x2
                y += y1 - y2

            x, y = x2, y2
            while 0 <= x < h and 0 <= y < w:
                s.add((x, y))
                x -= x1 - x2
                y -= y1 - y2

            '''
            x3 = x1 + (x1 - x2)
            y3 = y1 + (y1 - y2)
            x4 = x2 - (x1 - x2)
            y4 = y2 - (y1 - y2)
            if 0 <= x3 < h and 0 <= y3 < w:
                s.add((x3, y3))
            if 0 <= x4 < h and 0 <= y4 < w:
                s.add((x4, y4))
            '''
print(len(s))


