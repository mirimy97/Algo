import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = input()
    B = input()
    diff = {'W': 0, 'B': 0}
    for i in range(N):
        if A[i] != B[i]:
            diff[A[i]] += 1
    print(max(diff.values()))