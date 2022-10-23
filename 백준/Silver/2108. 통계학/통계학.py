import sys
from collections import Counter

N = int(input())
q = []
for _ in range(N):
    q.append(int(sys.stdin.readline().strip()))
print(round(sum(q)/len(q)))
q.sort()
print(q[len(q)//2])
cnt = Counter(q)
most = cnt.most_common()
if len(most) > 1 and most[0][1] == most[1][1]:
    print(most[1][0])
else:
    print(most[0][0])
print(max(q) - min(q))