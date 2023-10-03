import sys
input = sys.stdin.readline

N, K = map(int, input().split())
H = list(map(int, input().split()))

diff = [0] * (N - 1)
for i in range(N - 1):
    diff[i] = H[i + 1] - H[i]
diff.sort()
print(sum(diff[:N-K]))
