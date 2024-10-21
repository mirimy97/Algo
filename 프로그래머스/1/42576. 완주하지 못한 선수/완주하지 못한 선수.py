def solution(participant, completion):
    h = {}
    for c in completion:
        if c in h:
            h[c] += 1
        else:
            h[c] = 1
    for p in participant:
        if p not in h or h[p] == 0:
            return p
        else:
            h[p] -= 1
            