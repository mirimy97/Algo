import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

V = [0] * N
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    if not V[A]:
        v = [0] * N
        q = deque([A])
        v[A] = 1
        while q:
            s = q.popleft()
            for e in range(N):
                if not v[e] or v[e] > v[s] + arr[s][e]:
                    v[e] = v[s] + arr[s][e]
                    q.append(e)
        V[A] = v
    if V[A][B] - 1 <= C:
        print('Enjoy other party')
    else:
        print('Stay here')