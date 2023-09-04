import sys
input = sys.stdin.readline

def rank(n):
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(n // i, N)
    return cnt

N = int(input())
k = int(input())

left = 1
right = k
ans = 0
while left <= right:
    middle = (left + right) // 2    # idx 번째에 있는 값 B[k]
    count = rank(middle)
    if count < k:
        left = middle + 1
    elif count >= k:
        right = middle - 1
        ans = middle
print(ans)