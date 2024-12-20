import time
f = open('day19input')
st  = time.time()
lines = f.read().splitlines()

patterns = list(lines[0].split(', '))
designs = lines[2:]

res = 0
res2 = 0
for design in designs:
    dp = [0 for x in design]
    for i in range(len(dp)):
        for pattern in patterns:
            if i + 1 >= len(pattern):
                if design[i - len(pattern) + 1 : i+1] == pattern:
                    if i - len(pattern) == -1:
                        dp[i] += 1
                    else:
                        dp[i] += dp[i - len(pattern)]
    # print(dp[-1])
    res += dp[-1] != 0
    res2 += dp[-1]

print(res)
print(res2)
print('time ', time.time() - st)


