import sys
input = sys.stdin.readline

def perm(i, n):
    if i == n:
        score = 0
        for j in range(len(arr)):
            if arr[j] == ans[j]:
                score += 1
        if score >= 5:
            global cnt
            cnt += 1
    else:
        for a in range(1, 6):
            ans[i] = a
            if not(i > 1 and ans[i - 1] == ans[i - 2] == ans[i]):
                perm(i + 1, n)
            ans[i] = 0

arr = list(map(int, input().split()))
ans = [0] * len(arr)
cnt = 0
perm(0, len(arr))

print(cnt)