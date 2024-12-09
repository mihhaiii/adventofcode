import bisect
import time
start_time = time.time()
start_time_c = time.perf_counter()
start_time_p = time.process_time()
with open('day9Input') as f:
    a = [int(x) for x in f.read().strip()]
    b = []
    is_file = True
    file_id = 0

    free = [{} for _ in range(10)]
    for i, x in enumerate(a):
        if is_file:
            b += [file_id for _ in range(x)]
            file_id += 1
        else:
            free[x][len(b)] = None
            b += [-1 for _ in range(x)]
        is_file = not is_file

    c = [x for x in b]

    i = 0
    j = len(b) - 1
    while i < j:
        while b[i] != -1: i += 1
        while b[j] == -1: j -= 1
        if i >= j: break
        b[i], b[j] = b[j], b[i]
        i += 1
        j -= 1

    current_pos = len(b)
    for i in range(len(a) - 1, -1, -1):
        current_pos -= a[i]
        id = i // 2
        if i % 2 == 0: # is file
            found = False
            min_idx = len(b)
            min_idx_len = -1
            for l in range(a[i], 10):
                if free[l]:
                    found = True
                    curr_idx = next(iter(free[l]))
                    if curr_idx < min_idx:
                        min_idx, min_idx_len = curr_idx, l
            if found and min_idx < current_pos:
                for j in range(min_idx, min_idx + a[i]):
                    c[j] = id
                for j in range(current_pos, current_pos + a[i]):
                    c[j] = -1
                free[min_idx_len].pop(next(iter(free[min_idx_len])))
                new_len = min_idx_len - a[i]
                if new_len:
                    #pos = bisect.bisect(free[new_len], min_idx + a[i])
                    #free[new_len].insert(pos, min_idx + a[i])
                    free[new_len][min_idx + a[i]] = None

    ans = sum([i * x for i, x in enumerate(b) if x != -1])
    ans2 = sum([i * x for i, x in enumerate(c) if x != -1])
    print(ans)
    print(ans2)
    print(f'time = {(time.time() - start_time):.2f} seconds')
    print(f'time = {time.perf_counter() - start_time_c:.2f} seconds')
    print(f'time = {time.process_time() - start_time_p:.2f} seconds')
