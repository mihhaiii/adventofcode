f = open('day17Input')

for line in f:
    if line.startswith('Register'):
        value = int(line.split(':')[-1].strip())
        if line.find('A:') != -1:
            A = value
        elif line.find('B:') != -1:
            B = value
        else:
            C = value
    elif line.startswith('Program'):
        ops = [int(x) for x in line.split(': ')[-1].strip().split(',')]
print(A, B, C)
print(ops)
def combo_f(x):
    if x <= 3:
        return x
    if x == 4: return A
    if x == 5: return B
    if x == 6: return C

I = 0
out = []
'''
while I < len(ops):
    op = ops[I]
    literal = ops[I + 1]
    combo = combo_f(literal)
    jump = False
    if op == 0:
        A = A // (2 ** combo)
    elif op == 1:
        B ^= literal
    elif op == 2:
        B = combo % 8
    elif op == 3:
        if A:
            I = literal
            jump = True
    elif op == 4:
        B ^= C
    elif op == 5:
        out.append(combo % 8)
    elif op == 6:
        B = A // (2 ** combo)
    elif op == 7:
        C = A // (2 ** combo)
    if not jump:
        I += 2
'''
def f(A):
    out = []
    while True:
        B = A % 8
        B ^= 1
        C = A // (2 ** B)
        A = A // 8
        B ^= 4
        B ^= C
        out.append(B % 8)
        if A == 0:
            break
    #print(','.join([str(x) for x in out]))
    return out[0]


a = [0]
for v in reversed(ops):
    b = []
    for A in a:
        for prevA in range(A * 8, A * 8 + 8):
            if f(prevA) == v:
                b.append(prevA)
    a = b
    print(f'for result {v}: a is ', a)
print(min(a))

