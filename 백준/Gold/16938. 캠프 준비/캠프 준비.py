import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# 2문제 이상
# L <= (문제 난이도 합) <= R
# 어려운 문제 - 쉬운 문제 >= X
def perm(i, n, L, R):
    global cnt
    if i == n:
        if L <= 0 and R >= 0:
            cnt += 1
    else:
        perm(i + 1, n, L, R)
        perm(i + 1, n, L - arr[i], R - arr[i])

cnt = 0
for s in range(N):
    for e in range(s + 1, N):
        if A[e] - A[s] >= X:
            temp_R = R - (A[s] + A[e])
            temp_L = L - (A[s] + A[e])
            arr = A[s + 1 : e]
            perm(0, len(arr), temp_L, temp_R)
print(cnt)