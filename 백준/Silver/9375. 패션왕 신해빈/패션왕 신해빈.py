from collections import deque, Counter

T = int(input())
for _ in range(T):
    clo = deque()
    N = int(input())
    for _ in range(N):
        a, b = input().split()
        clo.append(b)
    common = Counter(clo).most_common()
    result = 1
    for i in range(len(common)):
        result *= (common[i][1] + 1)
    print(result - 1)