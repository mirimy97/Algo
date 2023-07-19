import sys
from heapq import heappush, heappop

N, M = map(int, sys.stdin.readline().split())
A, B, K, G = map(int, sys.stdin.readline().split())
# 고둘라가 방문하는 교차로
g_road = list(map(int, sys.stdin.readline().split()))
# 도로 정보
arr = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    U, V, L = map(int, sys.stdin.readline().split())
    arr[U][V] = L
    arr[V][U] = L

# 고둘라가 이 시간대 t에 어디에 있냐..(a, b) a시에 b에 있다
gt = - K
g = g_road[:]
g[0] = (gt, g_road[0])
for i in range(1, G):
    gt += arr[g_road[i - 1]][g_road[i]]
    g[i] = (gt, g_road[i])
# bfs
# q에 저장하는데, 출발하는 시간t랑 같이저장
# 출발하는 시간 t에 고둘라 걸려있으면 그 시간가지 + 해서 가중치 저장

q = [[0, A]]
v = [0] * (N + 1)
while q:
    t, s = heappop(q)
    for e in range(1, N + 1):
        # e 까지 가는 시간 계산
        for i in range(G - 1):
            if t >= g[i][0]:
                gs = g[i][1]
                ge = g[i + 1][1]
                t_end = g[i + 1][0]
            else:
                break
        # 갈 수 있나?
        if arr[s][e]:
            # 내가 가는 길이랑 겹치나?
            if {s, e} == {gs, ge}:
                # 가중치= 출발t + 실제 걸리는 시간 + (t_end - 지금t)
                new_t = arr[s][e] + t_end
            else:
                new_t = t + arr[s][e]
            if not v[e] or new_t < v[e]:
                v[e] = new_t
                heappush(q, [new_t, e])
print(v[B])
