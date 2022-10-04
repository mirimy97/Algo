N = int(input())
A = set(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))

for b in B:
    if not A & set([b]):
        print(0)
    else:
        print(1)