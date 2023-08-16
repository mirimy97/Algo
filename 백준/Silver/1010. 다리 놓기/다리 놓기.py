import sys, math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    answer = math.factorial(M) / (math.factorial(N) * math.factorial(M-N))
    print(int(answer))