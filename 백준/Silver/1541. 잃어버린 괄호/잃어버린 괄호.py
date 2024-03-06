import sys
input = sys.stdin.readline
A = input() + "+"
s = 0
ans = 0
minus = 0
for i in range(len(A) + 1):
    if i == len(A):
        pass
    elif A[i] == "-":
        if minus == 0:
            ans += int(A[s:i])
        else:
            ans -= int(A[s:i])
        minus = True
        s = i + 1
    elif A[i] == "+":
        if minus:
            ans -= int(A[s:i])
        else:
            ans += int(A[s:i])
        s = i + 1
print(ans)