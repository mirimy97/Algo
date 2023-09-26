import sys
from itertools import combinations
input = sys.stdin.readline

C = list(map(int, input().split()))
answer = [0, 0] # 짝, 홀
for n in range(1, 4):
    for c in combinations(C, n):
        val = 1
        for v in c:
            val *= v
        answer[val % 2] = max(answer[val % 2], val)

if answer[1]:
    print(answer[1])
else:
    print(answer[0])