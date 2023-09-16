import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
box = list(map(int, input().split()))
result = [0]
for i in range(n):
    idx = bisect_left(result, box[i])
    if idx == len(result):
        result.append(box[i])
    else:
        result[idx] = box[i]
print(len(result) - 1)