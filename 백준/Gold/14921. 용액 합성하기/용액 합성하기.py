import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))
left, right = 0, N-1
answer, pre = 200000000, 200000000
while left < N-1:
    cur = A[left] + A[right]
    if abs(answer) >= abs(cur):
        answer = cur
    if pre >= abs(cur):
        pre = cur
        right -= 1
    else:
        right += 1
        left += 1
        pre = 200000000
    if left == right:
        left += 1
        right += 1
print(answer)