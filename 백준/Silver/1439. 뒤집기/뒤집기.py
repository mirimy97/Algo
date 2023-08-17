nums = input()
q = []
for n in nums:
    if not q:
        q.append(n)
    elif q[-1] != n:
        q.append(n)
print(min(q.count('0'), q.count('1')))