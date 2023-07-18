import sys
from heapq import heappush, heappop

def dij(start, end):
    v = [0] * V  # visited
    v[start] = 1
    heap = [(1, start)]
    while heap and not v[end]:
        cost, now = heappop(heap)
        if v[now] and v[now] < cost:
            continue
        v[now] = cost
        for next in range(V):
            if not v[next] and arr[now][next] != 10001:
                heappush(heap, (v[now] + arr[now][next], next))

    return v[end] - 1

V, E, P = map(int, sys.stdin.readline().split())
arr = [[10001] * V for _ in range(V)]
for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a - 1][b - 1] = c
    arr[b - 1][a - 1] = c

if dij(0, V - 1) == dij(0, P - 1) + dij(P - 1, V - 1):
    print("SAVE HIM")
else:
    print("GOOD BYE")