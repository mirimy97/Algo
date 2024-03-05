import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

sorted_X = sorted(list(set(X)))
for x in X:
    print(bisect_left(sorted_X, x), end=" ")
