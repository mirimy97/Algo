import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    print(sum(A[i - 1:j]))