import sys
N = int(input())
arr = [0] * N
for i in range(N):
    x, y = sys.stdin.readline().split()
    arr[i] = int(x), y

arr = sorted(arr, key = lambda x : (x[0]))

for n in range(N):
    print(arr[n][0], arr[n][1])