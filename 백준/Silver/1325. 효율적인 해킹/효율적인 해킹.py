import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
h = {i : [] for i in range(1, N + 1)}
cnt = [0] * (N + 1)    # (번호, cnt)
for _ in range(M):
    A, B = map(int, input().split())
    h[B].append(A)
for S in range(1, N + 1):
    q = deque([S])
    v = [0] * (N + 1)
    v[S] = 1
    while q:
        s = q.popleft()
        for e in h[s]:
            if not v[e]:
                q.append(e)
                cnt[S] += 1
                v[e] = 1
for i in range(1, N + 1):
    if cnt[i] == max(cnt):
        print(i, end=" ")