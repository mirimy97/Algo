import sys
T = int(input())
for _ in range(T):
    S = list(sys.stdin.readline().split())
    for s in S:
        print(s[::-1], end=" ")
    print()