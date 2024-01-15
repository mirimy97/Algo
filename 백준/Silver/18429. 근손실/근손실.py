import sys
input = sys.stdin.readline

def perm(i, n):    # 몇째날?
    global weight, cnt
    if i == n:
        cnt += 1
    else:
        for j in range(n):  # 몇번째 키트?
            if not v[j]:
                v[j] = 1
                weight += (A[j] - K)
                if weight >= 0:
                    perm(i + 1, n)
                weight -= (A[j] - K)
                v[j] = 0

N, K = map(int, input().split())
A = list(map(int, input().split()))
v = [0] * N
weight = 0
cnt = 0
perm(0, N)
print(cnt)