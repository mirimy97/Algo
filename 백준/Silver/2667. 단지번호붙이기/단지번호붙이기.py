import sys
from collections import deque

N = int(input())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

danji = 0
SD = []
D = [(1, 0), (-1, 0), (0, 1), (0 ,-1)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            sedae = 1
            danji += 1
            q = deque([(i, j)])
            arr[i][j] = 0
            while q:
                si, sj = q.popleft()
                for di, dj in D:
                    ni, nj = si + di, sj + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
                        arr[ni][nj] = 0
                        sedae += 1
                        q.append((ni, nj))
            SD.append(sedae)
print(danji)
for i in sorted(SD):
    print(i)