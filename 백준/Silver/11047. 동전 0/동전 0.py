import sys

N, K = map(int, input().split())
coin = [0] * N
for i in range(N):
    coin[i] = int(sys.stdin.readline().strip())

cnt = 0
for i in range(N-1, -1, -1):
    if K == 0:
        break
    cnt += K // coin[i]
    K = K % coin[i]
print(cnt)