import sys
N, K = map(int, sys.stdin.readline().split())
pies = list(map(int, sys.stdin.readline().split()))


s = sum(pies[:K]) # 3
max_s = s

for i in range(N):
    next_s = s - pies[i % N] + pies[(i + K) % N]
    if max_s < next_s:
        max_s = next_s
    s = next_s

print(max_s)