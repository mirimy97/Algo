import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
s = sum(H)

if s % 3 != 0:
    print("NO")
else:
    cnt = 0
    # 1. 결국. 나무가 자라는 일 수 (s / 3)
    # 2. 제한적으로 사용할 수 있는 +2 물뿌리개를 기준으로 //2 해서
    # 일 수만큼 +2 물뿌리개를 사용할 수 있다면, +1은 신경쓸 필요 없음
    for h in H:
        cnt += h // 2
    if cnt >= (s / 3):
        print("YES")
    else:
        print("NO")
