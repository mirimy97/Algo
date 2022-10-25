from collections import deque

N = int(input())
if N == 1:
    print(0)
else:
    cnt = [0] * (10**6 + 2)
    q = deque([1])

    while cnt[N] == 0:
        S = q.popleft()
        for E in [S+1, S*2, S*3]:
            if E <= 10**6 and cnt[E] == 0:
                cnt[E] = cnt[S] + 1
                q.append(E)
    print(cnt[N])


