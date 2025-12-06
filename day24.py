f = open('day24Input')

d = {}
g = {}
for line in f.read().splitlines():
    if line.find(':') != -1:
        e = line.split(':')
        d[e[0]] = int(e[1].strip())

    elif line.find(' -> ') != -1:
        e = line.split(' -> ')
        g[e[1]] = e[0].split()

print(g)
visited = set()
def solve(x):
    global visited
    if x in d:
        return d[x]
    if x in g:
        op = g[x]
        op1 = solve(op[0])
        op2 = solve(op[2])
        if op1 or op2:
            visited.add(op[0])
            visited.add(op[2])
            visited.add(x)
        if op[1] == 'XOR':
            return op1 ^ op2
        if op[1] == 'OR':
            return op1 or op2
        if op[1] == 'AND':
            return op1 and op2

def assign(ch, v):
    l = 45
    for i in range(l):
        bit = 1 << i & v != 0
        num = str(i)
        if len(num) < 2: num = '0' + num
        num = ch + num
        d[num] = int(bit)

def get_sum():
    res = []
    visited.clear()
    for x in g:
        if x[0] == 'z':
            res.append((x, solve(x)))

    res.sort()
    p = 1
    ans = 0
    for ch, bit in res:
        #d[ch] = bit
        ans += p * bit
        p *= 2
    #print('sum', ans)
    return ans

def show(ch):
    l = 45
    print(f'{ch}=', end='')
    for i in range(l):
        st = str(i)
        if len(st) < 2: st = '0' + st
        print(d[ch+st], end='')
    print()

a = 14552111
b = 2242
show('x')
assign('x', a)
show('x')
show('y')
assign('y', b)
show('y')
sum = get_sum()
#show('z')
print('correct: ', sum == a + b)
print(visited)
import random
from collections import defaultdict
def get_acc():
    num_c = defaultdict(int)
    num_w = defaultdict(int)
    acc = defaultdict(float)
    for i in range(5000):
        if i % 100 == 0:
            print(i)

        x = 1 << random.randint(0, 45) | 1 << random.randint(0, 45)
        y = 1 << random.randint(0, 45) | 1 << random.randint(0, 45)
        assign('x', x)
        assign('y', y)
        sum = get_sum()
        correct = sum == x + y
        #print(visited)
        for v in visited:
            if correct:
                num_c[v] += 1
            else:
                num_w[v] += 1

    for k in num_w:
        acc[k] = num_c[k] / (num_c[k] + num_w[k])
    return acc, num_c, num_w

#g['tnm'], g['njq'] = g['njq'], g['tnm']
#g['z09'], g['wpr'] = g['wpr'], g['z09']
#g['rvc'], g['rrs'] = g['rrs'], g['rvc']
#g['jgb'], g['z20'] = g['z20'], g['jgb']
e = sorted(['tnm', 'njq', 'z09', 'wpr', 'rvc', 'rrs', 'jgb', 'z20', 'kkp', 'hvk', 'rkf', 'jnn'])
acc, num_c, num_w = get_acc()

for i in e:
    print(i, acc[i], num_c[i], num_c[i] + num_w[i])
print(','.join(sorted(['tnm', 'njq', 'z09', 'wpr', 'rvc', 'rrs', 'jgb', 'z20', 'kkp'])))
print(g['z09'])
print(g['z20'])

ratios = []
for k in num_w:
    if k[0] not in 'xy':
        ratios.append((k, acc[k], num_c[k], num_c[k] + num_w[k]))
ratios.sort(key=lambda x: x[1])
print(ratios)
cand=[x for x in ratios if x[1] < 0.1]
print(cand)
print(len(cand))


# o = 'rrs'
# for i,_,_,_ in cand:
#     for j,_,_,_ in cand:
#         if i == j:
#             continue
#         g[i], g[j] = g[j], g[i]
#         throws = False
#         try:
#             acc, num_c, num_w = get_acc()
#         except Exception:
#             throws = True
#         if not throws and acc[i] > 0.1 and acc[j] > 0.1:
#             print('found pair', i, j, acc[i], acc[j])
#         g[i], g[j] = g[j], g[i]
#
