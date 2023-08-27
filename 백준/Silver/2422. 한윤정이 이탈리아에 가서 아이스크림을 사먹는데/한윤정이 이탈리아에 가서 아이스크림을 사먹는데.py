import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[1] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 0
    arr[b][a] = 0
cnt = 0
for i in range(1, N-1):
    for j in range(i+1, N):
        if arr[i][j]:
            for k in range(j+1, N+1):
                if arr[i][k] and arr[j][k]:
                    cnt += 1
print(cnt)