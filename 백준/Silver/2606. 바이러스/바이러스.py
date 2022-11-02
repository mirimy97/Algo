import sys
from collections import deque

C = int(input())
N = int(input())
arr = [[0] * (C+1) for _ in range(C+1)]
for _ in range(N):
    c1, c2 = map(int, sys.stdin.readline().split())
    arr[c1][c2] = 1
    arr[c2][c1] = 1

q = deque()
visited = [0] * (C+1)
S = 1
while True:
    for E in range(1, C+1):
        if arr[S][E] == 1 and not visited[E]:
            visited[E] = 1
            q.append(E)
    if q:
        S = q.pop()
    else:
        break
print(sum(visited) - 1)