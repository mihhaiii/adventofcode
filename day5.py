s = set()
ans = 0
ans2 = 0
with open('day5Input') as f:
    for line in f:
        if line:
            if line.find('|') != -1:
                a,b = map(int, line.strip().split('|'))
                s.add((a,b))
            elif line.find(',') != -1:
                a = list(map(int, line.strip().split(',')))
                ok = True
                for i in range(len(a)):
                    while True:
                        swapped = False
                        for j in range(i+1,len(a)):
                            if (a[j], a[i]) in s:
                                ok = False
                                swapped = True
                                a[i], a[j] = a[j], a[i]
                                break
                        if not swapped:
                            break
                if ok:
                    ans += a[len(a)//2]
                else:
                    ans2 += a[len(a)//2]
print(ans)
print(ans2)
