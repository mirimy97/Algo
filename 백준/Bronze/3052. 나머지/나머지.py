S = set()
for _ in range(10):
    n = int(input())
    S.add(n % 42)
print(len(S))
