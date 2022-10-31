
N = int(input())
A = [0] * 500001

cnt = 0
for i in range(224):
    if i == 1:
        cnt += 1
    for j in range(224):
        if i == 0 and j == 1:
            cnt += 1
        for k in range(224):
            if i == 0 and j == 0 and k == 1:
                cnt += 1
            for l in range(224):
                if i == 0 and j == 0 and k == 0 and l == 1:
                    cnt += 1
                num = i**2 + j**2 + k**2 + l**2
                if not A[num]:
                    A[num] = cnt
                if num > N:
                    break
            if A[N]:
                break
        if A[N]:
            break
    if A[N]:
        break
print(A[N])