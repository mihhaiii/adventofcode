import itertools

codes = open('day21Input').read().splitlines()

print(codes)
num_codes = [int(x[:-1]) for x in codes]

numeric = [['7', '8', '9'],
           ['4', '5', '6'],
           ['1', '2', '3'],
           ['#', '0', 'A']]

directional = [['#', '^', 'A'],
               ['<', 'v', '>']]

def get_path(a, b):
    if a in '<>^v' or b in '<>^v':
        m = directional
    else:
        m = numeric
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == a:
                i1, j1 = i, j
            if m[i][j] == b:
                i2, j2 = i, j

    def get_path_int(x1, y1, x2, y2):
        path = ''
        if x2 > x1:
            path += 'v' * (x2 - x1)
        elif x2 < x1:
            path += '^' * (x1 - x2)
        if y2 > y1:
            path += '>' * (y2 - y1)
        elif y2 < y1:
            path += '<' * (y1 - y2)
        return path

    paths = set()
    for (x, y) in [(i1, j2), (i2, j1)]:
        if m[x][y] != '#':
            paths.add(get_path_int(i1, j1, x, y) + get_path_int(x, y, i2, j2))
    return list(paths)

def solve_list(s, it):
    sum = ''
    L = 0
    for x in s:
        l = solve(x, it)
        L += l
    return L + len(s)

from functools import lru_cache
@lru_cache(maxsize=None)
def solve(s, it):
    print(s, it)
    if it == 0:
        return len(s)
    if len(s) == 0:
        return 0
    prev = 'A'
    prods = []
    for x in s + 'A':
        paths = get_path(prev, x)
        prods.append(paths)
        prev = x

    min = -1
    for comb in itertools.product(*prods):
        current = 0
        l = 0
        for c in comb:
            l += solve(c, it - 1)
        if min == -1 or l < min:
            min = l

    return len(s) + min

res = 0
for i, code in enumerate(codes):
    all_paths = []
    prev = 'A'
    for x in code:
        paths = get_path(prev, x)
        prev = x
        all_paths.append(paths)
    print(all_paths)
    all_sol = [solve_list(list(x), 25) for x in itertools.product(*all_paths)]
    sol = min([x for x in all_sol])
    print(all_sol)
    print()
    res += num_codes[i] * sol

print(res)
