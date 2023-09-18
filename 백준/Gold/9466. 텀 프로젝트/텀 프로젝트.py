import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    team = list(map(int, input().split()))
    V = [0] * N
    cnt = 0
    for S in range(N):
        if V[S]: continue
        q = [S]
        while 1:
            s = q[-1]
            e = team[s] - 1
            V[s] = 1
            if V[e] == 1:
                for i in range(len(q)):
                    if q[i] == e:
                        cnt += len(q[i:])
                break
            q.append(e)
    print(N - cnt)