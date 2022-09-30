def newscore(n):
    return n/M*100

N = int(input())
scores = list(map(int,input().split()))

M = max(scores)
scores = list(map(newscore, scores))

print(sum(scores) / len(scores))