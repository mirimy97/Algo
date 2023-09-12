import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
D = [(1, 0), (0, 1)]
q = deque([[0, 0]])
v = [[0] * N for _ in range(N)]
while q:
    si, sj = q.popleft()
    for di, dj in D:
        n = arr[si][sj]
        ni, nj = si + (di * n), sj + (dj * n)
        if 0 <= ni < N and 0 <= nj < N and not v[ni][nj]:
            q.append([ni, nj])
            v[ni][nj] = 1
            if arr[ni][nj] == -1:
                print('HaruHaru')
                sys.exit(0)
print('Hing')