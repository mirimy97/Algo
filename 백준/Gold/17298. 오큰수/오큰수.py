import sys
from collections import deque
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
ans = ['-1'] * N
stack = deque()
for i in range(N):
    if not stack or stack[-1][1] >= A[i]:
        stack.append([i, A[i]])
    else:
        while stack and stack[-1][1] < A[i]:
            pi, pa = stack.pop()
            ans[pi] = str(A[i])
        stack.append([i, A[i]])
print(' '.join(ans))