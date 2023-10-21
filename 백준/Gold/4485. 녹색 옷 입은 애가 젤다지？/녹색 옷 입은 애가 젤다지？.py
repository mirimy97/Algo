import sys
from collections import deque
input = sys.stdin.readline

D = [(0, 1), (1, 0), (-1, 0), (0, -1)]
tc = 0
while 1:
    tc += 1
    N = int(input())
    if N:
        MAX_SIZE = 9 * N * N
        arr = [list(map(int, input().split())) for _ in range(N)]
        q = deque([[0, 0]])
        v = [[MAX_SIZE] * N for _ in range(N)]
        v[0][0] = arr[0][0]
        while q:
            si, sj = q.popleft()
            for di, dj in D:
                ni, nj = si + di, sj + dj
                if 0 <= ni < N and 0 <= nj < N and v[ni][nj] > v[si][sj] + arr[ni][nj]:
                    q.append([ni, nj])
                    v[ni][nj] = v[si][sj] + arr[ni][nj]
        print(f'Problem {tc}: {v[N - 1][N - 1]}')
    else:
        break