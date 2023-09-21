import sys
input = sys.stdin.readline

N, K = map(int, input().split())
X = [0] * N
for i in range(N):
    X[i] = int(input())
X.append(sys.maxsize)
X.sort()
ans = X[0]
i = 1
while i < len(X):
    lv_up = min(X[i] - X[i - 1], K // i)
    K -= lv_up * i
    ans += lv_up
    if K <= 0:
        break
    i += 1
print(ans)