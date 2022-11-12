import sys
from collections import deque

N, M = map(int, input().split())

arr = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    arr[u][v] = 1
    arr[v][u] = 1

cnt = 0
visited = [0] * (N+1)
for V in range(1, N+1):
    if visited[V] == 0:
        cnt += 1

        q = deque([V])
        visited[V] = 1

        while q:
            S = q.pop()

            for E in range(1, N+1):
                if arr[S][E] == 1 and not visited[E]:
                    q.append(E)
                    visited[E] = 1
print(cnt)