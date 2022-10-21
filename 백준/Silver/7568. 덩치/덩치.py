import sys

N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    cnt = 1
    for j in range(N):
        if i != j and arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    print(cnt, end=' ')