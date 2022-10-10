N = int(input())
a = len(str(N)) * 9
if N > a:
    start = N - a
else:
    start = 0
for i in range(start, N):
    cnt = i
    s = i
    while s != 0:
        cnt += s % 10
        s = s // 10
    if cnt == N:
        break
    else:
        i = 0
print(i)