import sys
from collections import deque

def print_style(x):
    if not x:
        return str(x)
    return str(x - 1)

n = int(sys.stdin.readline()) # 도시
m = int(sys.stdin.readline()) # 버스
arr = [[100001] * n for _ in range(n)]
for i in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    arr[a - 1][b - 1] = min(arr[a - 1][b - 1], cost)

for start in range(n):
    visited = [0] * n

    # bfs
    q = deque([start])
    visited[start] = 1
    while q:
        start = q.popleft()
        for end in range(n):
            if (not visited[end] or visited[end] > visited[start] + arr[start][end]) and arr[start][end] != 100001:
                if end not in q:
                    q.append(end)
                visited[end] = visited[start] + arr[start][end]
    print(" ".join(map(print_style, visited)))

