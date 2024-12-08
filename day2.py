ans = 0


def safe(a):
    ok = True
    inc = False
    dec = False
    for i in range(len(a) - 1):
        x = a[i]
        y = a[i + 1]
        diff = x - y
        if abs(diff) not in [1,2,3]:
            ok = False
        if diff < 0:
            inc = True
        elif diff > 0:
            dec = True

    if inc and dec:
        ok = False

    return 1 if ok else 0

with open('day2Input') as f:
    for line in f:
        a = [int(x) for x in line.split()]

        indices = []
        for i in range(len(a) - 1):
            x = a[i]
            y = a[i + 1]
            diff = x - y
            if abs(diff) not in [1,2,3]:
                indices += [i, i + 1]
            if i < len(a) - 2:
                if (a[i] - a[i + 1]) * (a[i + 1] - a[i + 2]) < 0:
                    indices += [i, i + 1, i + 2]

        if safe(a):
            ans += 1
        else:
            for ind in indices:
                b = a[:ind] + a[ind+1:]
                if safe(b):
                    ans += 1
                    break


print(ans)
