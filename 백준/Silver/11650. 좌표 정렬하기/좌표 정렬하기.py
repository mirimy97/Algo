import sys

N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, sys.stdin.readline().split()))

arr = sorted(arr, key = lambda x : (x[0], x[1]))

for n in range(N):
    print(arr[n][0], arr[n][1])