from collections import defaultdict
from heapq import heapify, heappop, heappush
grid = []
f = open('day16Input')
for line in f:
    grid.append(line.strip())

h = len(grid)
w = len(grid[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
node_count = 0
graph = defaultdict(list)

# create weighed graph
for i in range(h):
    for j in range(w):
        if grid[i][j] != '#':
            for d in range(4):
                node_count += 1
                dir = dirs[d]
                x, y = i + dir[0], j + dir[1]
                if 0 <= x < h and 0 <= y < w and grid[x][y] != '#':
                    graph[(i, j, d)].append((x, y, d, 1))
                graph[(i, j, d)] += [(i, j, (d - 1) % 4, 1000), (i, j, (d + 1) % 4, 1000)]
        if grid[i][j] == 'S':
            start = i, j
        if grid[i][j] == 'E':
            end = i, j

# compute dist from start node to all others
def compute_dist(start_node):
    dist = {}
    for node in graph:
        dist[node] = 10 ** 18

    dist[start_node] = 0
    q = []
    heappush(q, (0, start_node))

    removed = set()
    while len(q) != 0:
        curr_dist, (x, y, d) = heappop(q)
        if (x, y, d) in removed:
            continue

        for nx, ny, nd, length in graph[(x, y, d)]:
            curr_dist_to_next = dist[(nx, ny, nd)]
            if curr_dist + length < curr_dist_to_next:
                removed.add((nx, ny, curr_dist_to_next))
                curr_dist_to_next = curr_dist + length
                dist[(nx, ny, nd)] = curr_dist_to_next
                heappush(q, (curr_dist_to_next, (nx, ny, nd)))
    return dist

# part 1
start_node = start[0], start[1], 1
dist = compute_dist(start_node)
res = min([dist[(end[0], end[1], d)] for d in range(4)])

# part 2; compute dist from end node to all others
# and check if cells are on a shortest path by checking
# if dist(start, cell) + dist(cell, end) == dist(start, end) (computed in part 1)
dist_e = [{} for d in dirs]
for d in range(4):
    dist_e[d] = compute_dist((end[0], end[1], d))

res2 = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] != '#':
            found = False
            for d in range(4):
                for end_d in range(4):
                    dist_start_cell = dist[(i, j, d)]
                    opp = lambda x: dirs.index((-dirs[x][0], -dirs[x][1]))
                    dist_cell_end = dist_e[opp(end_d)][(i, j, opp(d))]
                    if dist_start_cell + dist_cell_end == res:
                        found = True
            if found:
                res2 += 1

print(res)
print(res2)
