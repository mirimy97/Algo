import sys
input = sys.stdin.readline

N = int(input())
work = [[0, 0] for _ in range(N)]
for i in range(N):
    T, S = map(int, input().split())
    work[i] = (S, T)    # (끝나는 시간 / 걸리는 시간)
work.sort()

t = work[len(work) - 1][0]
while work:
    e, wt = work.pop()
    if t > e:
        t = e
    t -= wt
    if t < 0:
        t = -1
        break
print(t)