from collections import deque

N, K = map(int, input().split())
if N >= K:
    print(N - K)
else:
    visited = [0] * (K+2)
    q = deque([N])
    visited[N] = 1
    while visited[K] == 0:
        S = q.popleft()
        for E in [S-1, S+1, 2*S]:
            if 0 <= E <= K+1 and not visited[E]:
                q.append(E)
                visited[E] = visited[S] + 1
    print(visited[K] - 1)