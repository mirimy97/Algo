import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    # A[r,c] = A[r][c]

    si = [0] * N
    sj = [0] * N
    for i in range(N):
        for j in range(N):
            si[i] += A[i][j]
            sj[i] += A[j][i]

    for _ in range(M):
        r1, c1, r2, c2, v = map(int, input().split())
        for i in range(r1 - 1, r2):
            si[i] += (v * (c2 - c1 + 1))
        for j in range(c1 - 1, c2):
            sj[j] += (v * (r2 - r1 + 1))
    print(*si)
    print(*sj)
