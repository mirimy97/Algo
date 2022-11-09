M, i, j = map(int, input().split())
cnt = 0
for N in range(M, 0, -1):
    # 1사분면
    if i < (2 ** (N-1)) and j < (2 ** (N-1)):
        cnt += 0
    # 2사분면
    elif i < (2 ** (N-1)) and j >= (2 ** (N-1)):
        cnt += 4 ** (N-1)
    # 3사분면
    elif i >= (2 ** (N-1)) and j < (2 ** (N-1)):
        cnt += (4 ** (N-1)) * 2
    # 4사분면
    else:
        cnt += (4 ** (N-1)) * 3
    i, j = i % (2 ** (N-1)), j % (2 ** (N-1))
print(cnt)