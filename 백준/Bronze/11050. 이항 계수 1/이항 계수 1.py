A, B = map(int, input().split())
ans = 1
for a in range(A, A-B, -1):
    ans *= a
for b in range(1, B+1):
    ans /= b
print(int(ans))