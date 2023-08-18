import sys, copy
input = sys.stdin.readline

N, M = map(int, input().split())
W = sorted(list(map(int, input().split())))

for i in range(M-1):
    for j in range(i+1, M):
        if W[i] + W[j] > N:
            break
        W.append(W[i] + W[j])

memo = [N+1] * (N+1)  # 짜장면 n그릇까지 도달할 수 있는 최소 횟수
memo[N] = 1
next = set([N])  # 고려해야 할 것

cnt = 0
while memo[0] == N+1:
    cnt += 1
    roof = copy.deepcopy(next)
    next = set()
    remain = len(roof) * len(W)
    for r in roof:
        for w in W:
            if r - w >= 0:
                memo[r - w] = min(memo[r - w], memo[r] + 1)
                next.add(r - w)
            else:
                remain -= 1
            if memo[0] != N+1:
                print(cnt)
                sys.exit(0)
    if not remain:
        cnt = -1
        break       
print(cnt)