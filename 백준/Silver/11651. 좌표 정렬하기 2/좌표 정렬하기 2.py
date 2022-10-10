N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda x : [x[1], x[0]])

for a in arr:
    print(a[0], a[1])