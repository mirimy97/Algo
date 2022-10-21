N = int(input())
arr = list(map(int, input().split()))

cnt = 0
for idx in range(N):
    if arr[idx] > 1:
        is_prime = True
        for i in range(2, int((arr[idx])**(1/2)) + 1):
            if arr[idx] % i == 0:
                is_prime = False
                break
        if is_prime:
            cnt += 1

print(cnt)