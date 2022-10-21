import sys
N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = int(sys.stdin.readline().strip())
arr.sort()
for a in arr:
    print(a)