import sys
import copy
input = sys.stdin.readline

N, S, M = map(int, input().split())
V = list(map(int, input().split()))
arr = [-1] * (M + 1)
arr[S] = 0
for i in range(N):   # 볼륨 순번
    new_arr = copy.deepcopy(arr)
    for v in range(M + 1):    # 볼륨
        if arr[v] == i:
            if 0 <= v - V[i] <= M:
                new_arr[v - V[i]] = i + 1
            if 0 <= v + V[i] <= M:
                new_arr[v + V[i]] = i + 1
    arr = new_arr
for i in range(M, -1, -1):
    if arr[i] == N:
        print(i)
        sys.exit(0)
print(-1)