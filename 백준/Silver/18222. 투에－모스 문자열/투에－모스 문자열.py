import sys
input = sys.stdin.readline

k = int(input())
X = [0, 1]

cnt = 0
while k > 2:
    n = 0
    while k > 2 ** n:
        n += 1
    n -= 1
    cnt += 1
    k -= 2 ** n

if cnt % 2 == 1:
    print(int(not X[k - 1]))
else:
    print(X[k - 1])