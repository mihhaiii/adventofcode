with open('day3Input') as f:
    s = f.read().strip()

print(s)

ans = 0


def digit(s):
    res = 0
    for x in s:
        if x < '0' or x > '9':
            return -1
        res = res * 10 + (ord(x) - ord('0'))
    return res


# print(digit("542"))

allow = True
for i in range(len(s)):
    if i + 4 < len(s) and s[i:i + 4] == "do()":
        allow = True
    elif i + 7 < len(s) and s[i:i + 7] == "don't()":
        allow = False

    for l in range(8, 13):
        if i + l >= len(s):
            continue
        t = s[i:i + l]
        # print(t)
        if t[:4] == 'mul(' and t[-1] == ')':
            inner = t[4:-1]
            comma = inner.find(',')
            # print(inner, comma)
            if comma != -1:
                first = digit(inner[:comma])
                second = digit(inner[comma + 1:])
                if first != -1 and second != -1:
                    ans += first * second * (allow == True)

print(ans)
