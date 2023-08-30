import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, d = map(int, input().split())
    arr[a].append((b, d))
    arr[b].append((a, d))

# # 여우 (정속)
v_fox = [float('inf')] * (N + 1)
v_fox[1] = 0
q = [(0, 1)]   # (cost, node)
while q:
    cost, s = heappop(q)
    if cost > v_fox[s]: continue
    for e, d in arr[s]:
        new_cost = cost + d
        if v_fox[e] > new_cost:
            heappush(q, (new_cost, e))
            v_fox[e] = new_cost

# 늑대 (변속)
v_wolf = [[float('inf'), float('inf')] for _ in range(N + 1)]   # [False일때, True일때]
q = [(0, 1, True)]    # (cost, node, t:가속/f:감속)
v_wolf[1][0] = 0
while q:
    cost, s, fast = heappop(q)
    if cost > v_wolf[s][not fast]: continue
    for e, d in arr[s]:
        if fast:
            new_cost = cost + (d / 2)
        else:
            new_cost = cost + (d * 2)
        if v_wolf[e][fast] > new_cost:
            v_wolf[e][fast] = new_cost
            heappush(q, (new_cost, e, not fast))

cnt = 0
for i in range(2, N + 1):
    if v_fox[i] < min(v_wolf[i]):
        cnt += 1
print(cnt)