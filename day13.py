from math import gcd
f = open('day13Input')

x, y = 0, 0
res = 0
for line in f:
    if line.strip() == "":
        continue
    i1 = int(line[line.find('X') + 2:line.find(',')].strip())
    i2 = int(line[line.find('Y') + 2:].strip())
    if line.startswith("Button A"):
        a1, a2 = i1, i2
    elif line.startswith("Button B"):
        b1, b2 = i1, i2
    elif line.startswith("Prize"):
        #c1, c2 = i1, i2 # part 1
        c1, c2 = i1 + 10000000000000, i2 + 10000000000000
        f1 = c1*b2 - c2*b1
        f2 = a1*b2 - a2*b1

        if f1 % f2 == 0 and f1 * f2 > 0:
            x = f1 // f2
            f1 = c1 - a1*x
            f2 = b1
            if f1 % f2 == 0 and f1 * f2 > 0:
                y = f1 // f2
                res += 3*x + y

print(res)
