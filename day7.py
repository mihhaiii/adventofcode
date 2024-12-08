import sys
import time
start_time = time.time()
sys.setrecursionlimit(1000)

ans = 0
a = []

def num_digits(x):
    res = 0
    while x:
        res += 1
        x //= 10
    return res

def gen(mask):
    global found
    if found:
        return
    if len(mask) == len(a) - 1:
        res = a[0]
        for i in range(1, len(a)):
            if mask[i-1] == 0:
                res += a[i]
            elif mask[i-1] == 1:
                res *= a[i]
            else:
                #res = res * (10 ** num_digits(a[i])) + a[i]
                res = int(f'{res}{a[i]}')
        if res == expected:
            found = True
        return
    gen(mask+[0])
    gen(mask+[1])
    gen(mask+[2])

global found
global expected
with open('day7Input') as f:
    for line in f:
        x, a = line.strip().split(": ")
        x = int(x)
        a = [int(x) for x in a.split()]
        #x = int(line[:line.find(':')])
        #a = list(map(int, line[line.find(':')+1:].strip().split()))

        '''
        for mask in range(1 << (len(a) - 1)):
            res = a[0]
            for i in range(1, len(a)):
                if (1 << (i - 1)) & mask:
                    res *= a[i]
                else:
                    res += a[i]
            if res == x:
                ans += x
                break
        '''

        expected = x
        found = False
        gen([])
        print(found)
        if found:
           ans += x




print(ans)
print(f"{time.time() - start_time} seconds")
