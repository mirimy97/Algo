import sys
n, m = map(int, sys.stdin.readline().split())
earns = list(map(int, sys.stdin.readline().split()))

e = sum(earns[:m])
max_e = e

for i in range(m, n):
    e = e + earns[i] - earns[i - m]
    max_e = max(max_e, e)

print(max_e)