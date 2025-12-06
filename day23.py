from typing import Set

f = open('day23Input')
from collections import defaultdict
graph = defaultdict(set)
for line in f.read().splitlines():
    a, b = line.split('-')
    graph[a].add(b)
    graph[b].add(a)

for g in graph.items():
    print(g)
print(graph)

visited = set()
cc = []
s = set()
p = defaultdict(str)
def dfs(node, par=''):
    visited.add(node)
    cc[-1].append(node)
    p[node] = par
    for next in graph[node]:
        if next not in visited:
            dfs(next, node)
        else:
            if p[p[node]] == next:
                s.add(tuple(sorted((node, p[node], next))))
for node in graph:
    if node not in visited:
        cc.append([])
        dfs(node)

print(s)
print(len(s))
print(sum(1 for x in s if sum(1 for y in x if y[0] == 't') != 0))


s.clear()
for a in graph:
    for b in graph[a]:
        for c in graph[b]:
            if c in graph[a]:
                s.add(tuple(sorted((a,b,c))))
print('ls', len(s))
print(sum(1 for x in s if sum(1 for y in x if y[0] == 't') != 0))

res2 = 0
res2_str = ''
from  functools import lru_cache
def solve(lan, pool : Set[str]):
    global res2
    global res2_str
    if len(pool) == 0:
        if len(lan) > res2:
            res2 = len(lan)
            res2_str = ','.join(sorted(list(lan)))
        return
    for new in pool:
        if new > lan[-1]:
            solve(lan + [new], pool & graph[new])

for x in graph:
    solve([x], graph[x])

print(res2)
print(res2_str)
