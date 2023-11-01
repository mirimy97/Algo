import sys
input = sys.stdin.readline

def perm(i, n, val):
    if i == n:
        global max_val, min_val
        max_val = max(max_val, val)
        min_val = min(min_val, val)
    else:
        for key in h:
            if h[key] > 0:
                h[key] -= 1
                perm(i + 1, n, int(eval(str(val) + key + A[i])))
                h[key] += 1

N = int(input())
A = list(input().split())
arr = list(map(int, input().split()))
h = {'+': arr[0], '-' : arr[1], '*' : arr[2], '/' : arr[3]}
max_val, min_val = -1000000000, 1000000000
perm(1, N, A[0])
print(max_val)
print(min_val)