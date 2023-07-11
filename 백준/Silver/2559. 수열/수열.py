import sys

N, K = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

s = sum(nums[:K])
max_s = s

for i in range(N - K):
    next_s = s - nums[i] + nums[i + K]

    if next_s > max_s:
        max_s = next_s

    s = next_s

print(max_s)