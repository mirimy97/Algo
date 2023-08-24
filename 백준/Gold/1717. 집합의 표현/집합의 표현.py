import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    while parent[x] != x:
        x = parent[x]
    return x

# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0 and a != b:
        union(a, b)
    if cmd == 1:
        if a == b or find(a) == find(b):
            print('YES')
        else:
            print('NO')