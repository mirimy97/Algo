import sys
from collections import deque

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for V in range(N):
    q = deque([V])
    visited = [0] * N
    while q:
        S = q.pop()
        for E in range(N):
            if not visited[E] and arr[S][E] == 1:
                visited[E] = 1
                q.append(E)
    print(*visited)