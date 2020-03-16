import sys
from collections import defaultdict

N = int(input())
d = defaultdict(lambda: 0)
for line in sys.stdin:
    line = list(line.strip()[::-1]) # reverse string and cast to list
    unit = 1
    for c in line:
        d[c] += unit
        unit *= 10

l = sorted(d.values(),reverse=True)
total = 0
for i, val in enumerate(l):
    total += val * (9-i)
print(total)