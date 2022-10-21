nums = list(map(int, input().split()))

s = 0
for num in nums:
    s += num ** 2

print(s % 10)