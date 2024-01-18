import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
cnt = [0] * (N + 1) 
for _ in range(M):
    A, B = map(int, input().split())
    arr[B].append(A)
for S in range(1, N + 1):
    q = deque([S])
    v = [0] * (N + 1)
    v[S] = 1
    while q:
        s = q.popleft()
        for e in arr[s]:
            if not v[e]:
                q.append(e)
                cnt[S] += 1
                v[e] = 1
for i in range(1, N + 1):
    if cnt[i] == max(cnt):
        print(i, end=" ")