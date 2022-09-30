T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    for s in S:
        for _ in range(R):
            print(s, end='')
    print()