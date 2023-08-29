import sys
input = sys.stdin.readline

def dfs(n, i, j, cal, cnt):
    if n == 2 * (N - 1):
        global max_val, min_val
        val = eval(cal)
        max_val = max(max_val, val)
        min_val = min(min_val, val)
    else:
        if cal[-1].isdigit():
            cal = "(" + cal + ")"
        if cnt[0] > 0:
            cnt[0] -= 1
            dfs(n+1, i, j+1, cal + arr[i][j+1], cnt)
            cnt[0] += 1
        if cnt[1] > 0:
            cnt[1] -= 1
            dfs(n + 1, i+1, j, cal + arr[i+1][j], cnt)
            cnt[1] += 1

N = int(input())
arr = [list(input().split()) for _ in range(N)]
cnt = [N-1, N-1]  # 오른쪽, 아래쪽으로 N-1번씩 가야함
max_val, min_val = -2147000000, 2147000000
dfs(0, 0, 0, arr[0][0], cnt)
print(max_val, min_val)