import time
from collections import defaultdict
from time import perf_counter
st = time.perf_counter()
nums = [int(x) for x in open('day22Input').read().splitlines()]

res = 0
m = defaultdict(int)
print(len(nums))
for x in nums:
    prev_y = x % 10
    diffs = []
    s = set()
    for _ in range(2000):
        x ^= x * 64
        x %= 16777216

        x ^= x // 32
        x %= 16777216

        x ^= x * 2048
        x %= 16777216

        y = x % 10
        diff = y - prev_y
        prev_y = y
        diffs += [diff]
        if len(diffs) >= 4:
            if tuple(diffs[-4:]) not in s:
                s.add(tuple(diffs[-4:]))
                m[tuple(diffs[-4:])] += y
    res += x


print(m)
print(res)
print(max(m.values()))
print('time ', time.perf_counter() - st)
