import sys

N = int(input())
M = int(input())
no = set(list(sys.stdin.readline().split()))

ch = 0
for cnt in range(500000):
    if N - cnt >= 0 and not set(str(N - cnt)) & no:
        ch = N - cnt
        break
    if not set(str(N + cnt)) & no:
        ch = N + cnt
        break

if len(str(ch)) + cnt > abs(100 - N):
    print(abs(100 - N))
else:
    print(len(str(ch)) + cnt)