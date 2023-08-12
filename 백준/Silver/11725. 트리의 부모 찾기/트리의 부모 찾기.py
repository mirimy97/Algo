import sys
from collections import deque

N = int(sys.stdin.readline())
arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e = map(int, sys.stdin.readline().split())
    arr[s].append(e)
    arr[e].append(s)
answer = [0] * (N + 1)
v = [0] * (N + 1)
q = deque([1])
while q:
    s = q.popleft()
    for e in arr[s]:
        if not v[e]:
            q.append(e)
            v[e] = 1
            answer[e] = s
for i in range(2, N + 1):
    print(answer[i])