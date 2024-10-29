from collections import deque

def solution(priorities, location):
    q = deque()
    n = len(priorities)
    i = 0
    v = [0] * n
    while sum(v) < n:
        if not v[i%n]:
            if q: 
                while q and (q[-1][0] < priorities[i%n]):
                    v[q.pop()[1]] = 0
            q.append([priorities[i%n], i%n])
            v[i%n] = 1
        i += 1
    
    for j in range(n):
        if q[j][1] == location:
            return j + 1
    return 0