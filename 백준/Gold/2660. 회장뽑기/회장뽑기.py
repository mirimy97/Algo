import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N + 1)]
while 1:
    x, y = map(int, input().split())
    if x == -1:
        break
    arr[x].append(y)
    arr[y].append(x)

cand = []    # 회장 후보 (점수, 번호)
for S in range(1, N + 1): # 한명씩 검사
    q = deque([S])
    V = [-1] * (N + 1)
    V[S] = 0
    while q:
        s = q.popleft()
        for e in arr[s]:
            if V[e] == -1:
                q.append(e)
                V[e] = V[s] + 1
    cand.append((max(V), S))
cand.sort()
result = []
for c in cand:
    if c[0] == cand[0][0]:
        result.append(c[1])
print(cand[0][0], len(result))
print(*result)