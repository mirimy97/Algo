from functools import reduce

def solution(clothes):
    hash = {'a': 1}
    for c in clothes:
        if c[1] not in hash:
            hash[c[1]] = 2
        else:
            hash[c[1]] += 1

    return reduce(lambda x,y : x*y, hash.values()) - 1
