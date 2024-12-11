import time
from functools import lru_cache


# try out decorator pattern
def print_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        ret = func(*args, **kwargs)
        print(f'{time.perf_counter() - start_time:.4f} seconds')
        return ret

    return wrapper


# read input
a = []
f = open('day11Input')
a = [int(x) for x in f.read().strip().split()]
f.close()

cache = {}


# part 2, recursive with memoization
def count(start, iterations):
    if (start, iterations) in cache:
        return cache[(start, iterations)]

    if iterations == 0:
        return 1

    res = 0
    if start == 0:
        res = count(1, iterations - 1)
    else:
        s = str(start)
        l = len(s)
        if l & 1:
            res = count(start * 2024, iterations - 1)
        else:
            l //= 2
            res = count(int(s[:l]), iterations - 1) + \
                  count(int(s[l:]), iterations - 1)

    cache[(start, iterations)] = res
    return res

# alternative method, use functools.lru_cache instead of manual caching
# seems a bit faster as well
@lru_cache(maxsize=None)
def count2(start, iterations):
    if iterations == 0:
        return 1

    if start == 0:
        return count2(1, iterations - 1)
    s = str(start)
    l = len(s)
    if l & 1:
        return count2(start * 2024, iterations - 1)
    l //= 2
    return count2(int(s[:l]), iterations - 1) + \
           count2(int(s[l:]), iterations - 1)


@print_time
def solve():
    print(sum([count(x, 75) for x in a]))


@print_time
def solve2():
    print(sum([count2(x, 75) for x in a]))


solve()
solve2()

'''
# part 1, bruteforce
start = 0
res = 0
for it in range(75):
    print(it)
    end = len(a)
    for i in range(start, end):
        if a[i] == 0:
            a.append(1)
        else:
            s = str(a[i])
            l = len(s)
            if l & 1:
                a.append(a[i] * 2024)
            else:
                l //= 2
                a += [int(s[:l]), int(s[l:])]
    print(a[start:end])
    start = end
    res = len(a) - start

print(res)
'''
