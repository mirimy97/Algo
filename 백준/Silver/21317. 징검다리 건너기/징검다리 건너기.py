import sys
input = sys.stdin.readline

N = int(input())
# 점프 +1 +2 : 돌의 번호에 따라
# 점프 +3 : 한 번 사용, k 에너지 소비
E = [0] * N
for i in range(N - 1):
    E[i] = list(map(int, input().split()))
K = int(input())
if N == 1:
    print(0)
elif N == 2:
    print(E[0][0])
elif N == 3:
    print(min(E[0][1], E[0][0] + E[1][0]))
else:
    min_val = sys.maxsize
    # 3칸 점프 쓴 위치 결정
    for jump3 in range(N - 1, 2, -1):
        # dp 수행
        dp = [0] * N    # idx 번째 돌에 도달할 때 까지 사용한 에너지
        dp[1] = E[0][0]    # 첫번째 -> 두번째
        for i in range(2, N):
            if i == jump3:
                 dp[i] = min(dp[i - 1] + E[i - 1][0], dp[i - 2] + E[i - 2][1], dp[i - 3] + K)
            else:
                dp[i] = min(dp[i - 1] + E[i - 1][0], dp[i - 2] + E[i - 2][1])
        min_val = min(min_val, dp[N - 1])
    print(min_val)