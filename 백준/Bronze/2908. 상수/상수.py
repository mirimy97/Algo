nums = list(input().split())
for i in range(len(nums)):
    nums[i] = nums[i][::-1]
print(max(int(nums[0]), int(nums[1])))