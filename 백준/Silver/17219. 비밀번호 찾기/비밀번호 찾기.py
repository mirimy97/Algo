import sys

N, M = map(int, input().split())
pw = dict()
for _ in range(N):
    arr = list(sys.stdin.readline().strip().split())
    pw[arr[0]] = arr[1]

for _ in range(M):
    site = sys.stdin.readline().strip()
    print(pw[site])