import sys
N = int(input())
arr = [0] * 20000005
nums = list(map(int, sys.stdin.readline().split()))

for num in nums:
    arr[num + 10000000] += 1

M = int(input())

ms = list(map(int, sys.stdin.readline().split()))
for m in ms:
    print(arr[m + 10000000], end=' ')