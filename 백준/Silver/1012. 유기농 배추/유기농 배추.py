import sys
from collections import deque

T = int(input())
for _ in range(T):
    J, I, K = map(int, input().split())
    arr = [[0] * J for _ in range(I)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1

    cnt = 0
    for i in range(I):
        for j in range(J):
            if arr[i][j] == 1:
                cnt += 1
                q = deque([(i, j)])
                while q:
                    si, sj = q.popleft()
                    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        ni, nj = si + di, sj + dj
                        if 0 <= ni < I and 0 <= nj < J and arr[ni][nj]:
                            q.append((ni, nj))
                            arr[ni][nj] = 0
    print(cnt)
