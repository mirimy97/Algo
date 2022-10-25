N = int(input())
arr = sorted(list(map(int, input().split())))
s = 0
for i in range(N):
    s += arr[i] * (N - i)

print(s)