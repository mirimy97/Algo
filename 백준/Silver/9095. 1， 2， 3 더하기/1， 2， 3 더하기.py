def hap(i):
    global result
    for num in (1, 2, 3):
        memo[i] = num
        result[sum(memo)] += 1
        if sum(memo) <= 11 and i <= 10:
            hap(i+1)
        memo[i] = 0

memo = [0] * 12
result = [0] * 20
hap(1)

T = int(input())
for _ in range(T):
    n = int(input())
    print(result[n])