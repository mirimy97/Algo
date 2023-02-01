import sys

def s(N):
    global summ
    summ += int(N)
    return summ

N, M = map(int, input().split())

summ = 0
arr = [0] + list(map(s, input().split()))

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(arr[e] - arr[s-1])