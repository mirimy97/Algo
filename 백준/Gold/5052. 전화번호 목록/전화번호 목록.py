import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # 전화번호의 수 n
    n = int(input())
    tel = [0] * n
    for i in range(n):
        tel[i] = input().rstrip()
    tel.sort()
    possible = True
    first = -1
    for num in tel:
        if num[0] != first:
            first = num[0]
            H = {}
        for i in range(1, len(num) + 1):
            if num[:i] in H:
                possible = False
        if not possible:
            break
        else:
            H[num] = 1
    if not possible:
        print('NO')
    else:
        print('YES')
    # 첫번째 수 저장