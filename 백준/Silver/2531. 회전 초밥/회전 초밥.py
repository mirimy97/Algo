import sys
input = sys.stdin.readline

def add_map(n):
    if n in choice:
        choice[n] += 1
    else:
        choice[n] = 1
def remove_map(n):
    choice[n] -= 1
    if not choice[n]:
        del choice[n]

N, D, k, c = map(int, input().split())
dish = [0] * N
choice = {c : 1}
for i in range(N):
    n = int(input())
    if i < k:
        add_map(n)
    dish[i] = n
dish = dish[:] + dish[:k-1]
max_dish = len(choice)
for i in range(N - 1):
    add_map(dish[i + k])
    remove_map(dish[i])
    max_dish = max(max_dish, len(choice))
print(max_dish)
