import sys
from collections import deque

def bfs(start, end):
    global V
    v = [0] * V  # visited

    q = deque([start])
    v[start] = 1
    while q:
        now = q.popleft()
        for next in range(V):
            if (not v[next] or v[next] > v[now] + arr[now][next]) and arr[now][next] != 10001:
                q.append(next)
                v[next] = v[now] + arr[now][next]
    return v[end]

V, E, P = map(int, sys.stdin.readline().split())
arr = [[10001] * V for _ in range(V)]
for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a - 1][b - 1] = c
    arr[b - 1][a - 1] = c

if bfs(0, V - 1) >= bfs(0, P - 1) + bfs(P - 1, V - 1) - 1:
    print("SAVE HIM")
else:
    print("GOOD BYE")