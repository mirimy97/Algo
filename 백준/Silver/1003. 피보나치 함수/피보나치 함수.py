import sys
from collections import deque

def fibo(N):
    if memo[N] != -1:
        return memo[N]
    else:
        N1 = fibo(N-1)
        N2 = fibo(N-2)
        memo[N] = [N1[0] + N2[0], N1[1] + N2[1]]
        return memo[N]

T = int(input())
a = [[1, 0], [0, 1]] + [-1] * 41
memo = deque(a)
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    result = fibo(N)
    print(result[0], result[1])