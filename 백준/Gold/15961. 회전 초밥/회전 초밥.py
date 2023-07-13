import sys

N, d, k, c = map(int, sys.stdin.readline().split())
nums = [0] * N
for n in range(N):
    nums[n] = int(sys.stdin.readline())

h = {}
h[c] = 1
for i in range(k):
    if nums[i] in h:
        h[nums[i]] += 1
    else:
        h[nums[i]] = 1

max_eat = 0
for i in range(N):
    # 추가
    h[nums[(i + k) % N]] = h.get(nums[(i + k) % N], 0) + 1
    # 삭제
    h[nums[i]] = h.get(nums[i], 0) - 1
    if h[nums[i]] == 0:
        del h[nums[i]]

    max_eat = max(max_eat, len(h))

print(max_eat)




