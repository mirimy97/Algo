N = int(input())

if N % 5 == 0:
    n5 = N // 5
else:
    n5 = (N // 5) + 1

if ((n5 * 5) - N) % 2 == 1:
    n5 += 1

n3 = ((n5 * 5) - N) // 2
n5 -= n3

if n5 * 5 + n3 * 3 != N or n3 < 0 or n5 < 0:
    print(-1)
else:
    print(n3 + n5)