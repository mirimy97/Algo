import sys
from collections import deque

N, M = map(int, input().split())
F = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    F[a][b] = 1
    F[b][a] = 1

max_s = [5000, 0]
for V in range(1, N+1):
    visited = [0] * (N+1)
    q = deque([V])
    visited[V] = 1
    while q:
        S = q.popleft()
        for E in range(1, N+1):
            if F[S][E] == 1 and not visited[E]:
                q.append(E)
                visited[E] = visited[S] + 1

    if sum(visited) < max_s[0]:
        max_s[0] = sum(visited)
        max_s[1] = V

print(max_s[1])
