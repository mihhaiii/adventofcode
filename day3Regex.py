import re

with open('day3Input') as f:
    s = f.read().strip()

exp = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

matches = re.findall(exp, s)

allow = True
res = 0
for match in matches:
    if match == "do()":
        allow = True
    elif match == "don't()":
        allow = False
    else:
        if allow:
            a, b = map(int, match[4:-1].split(','))
            res += a*b


print(res)
