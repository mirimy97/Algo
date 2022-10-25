import sys

N, M = map(int, input().split())
D = set()
B = set()
for _ in range(N):
    D.add(sys.stdin.readline().strip())

for _ in range(M):
    B.add(sys.stdin.readline().strip())

D = sorted(list(D & B))
print(len(D))
for d in D:
    print(d)