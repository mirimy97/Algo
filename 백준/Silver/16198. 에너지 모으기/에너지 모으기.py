import sys
input = sys.stdin.readline

def perm(n, arr):
    global energy, max_energy
    if n <= 2:
        max_energy = max(energy, max_energy)
        return
    else:
        for i in range(1, n - 1):
            new = arr[:i] + arr[i + 1:]
            val = arr[i - 1] * arr[i + 1]
            energy += val
            perm(n - 1, new)
            energy -= val

N = int(input())
arr = list(map(int, input().split()))
energy = 0
max_energy = 0
perm(N, arr)
print(max_energy)