from collections import deque
import sys

N, M, V = map(int, input().split())
route = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    s, e = map(int, sys.stdin.readline().strip().split())
    route[s][e] = 1
    route[e][s] = 1

q = [V]
while q:
    S = q.pop()
    if visited[S]:
        continue
    visited[S] = 1
    print(S, end=' ')
    for E in range(N, 0, -1):
        if not visited[E] and route[S][E] == 1:
            q.append(E)

print()
q = deque([V])
visited = [0] * (N+1)
visited[V] = 1
while q:
    S = q.popleft()
    print(S, end=' ')
    for E in range(1, N+1):
        if not visited[E] and route[S][E] == 1:
            q.append(E)
            visited[E] = 1