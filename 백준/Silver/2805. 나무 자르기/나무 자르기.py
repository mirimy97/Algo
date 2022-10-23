import sys
from collections import deque
N, M = map(int, input().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

s = 0
e = 1000000000
ans = deque()
while True:
    if s > e:
        break
    cnt = 0
    H = (s + e) // 2
    for h in arr:
        if h > H:
            cnt += h - H
    if cnt == M:
        ans.append(H)
        break
    elif cnt > M:
        ans.append(H)
        s = H + 1
    elif cnt < M:
        e = H - 1

    if s + 1 == e and (H == s or H == e):
        break

print(max(ans))