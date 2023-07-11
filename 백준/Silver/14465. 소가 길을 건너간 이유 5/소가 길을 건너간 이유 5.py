import sys
N, K, B = map(int, sys.stdin.readline().split())
errs = [0] * N
for _ in range(B):
    errs[int(sys.stdin.readline()) - 1] = 1

s = sum(errs[:K]) # 3
min_s = s

for i in range(N - K):
    next_s = s - errs[i] + errs[i + K]
    if min_s > next_s:
        min_s = next_s
    s = next_s

print(min_s)