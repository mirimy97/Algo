def solution(genres, plays):
    hash = {}
    hap = {}
    for i in range(len(genres)):
        if genres[i] not in hash:
            hash[genres[i]] = [[i, plays[i]], [-1,-1]]
            hap[genres[i]] = plays[i]

        #     첫번째보다 크면
        elif hash[genres[i]][0][1] < plays[i]:
            hash[genres[i]] = [[i, plays[i]],hash[genres[i]][0]]
            hap[genres[i]] += plays[i]

        #     첫번째랑 같으면
        elif hash[genres[i]][0][1] == plays[i]:
            hash[genres[i]] = [min(hash[genres[i]][0], [i, plays[i]]), max(hash[genres[i]][0], [i, plays[i]])]
            hap[genres[i]] += plays[i]
        #     두번째보다 크면
        elif hash[genres[i]][1][1] < plays[i]:
            hash[genres[i]] = [hash[genres[i]][0], [i, plays[i]]]
            hap[genres[i]] += plays[i]
        else:
            hap[genres[i]] += plays[i]

    sorted_hap = sorted(hap.items(), key = lambda item: item[1], reverse = True)
    answer = []
    for s in sorted_hap:
        for h in hash[s[0]]:
            if h[1] != -1:
                answer.append(h[0])
    return answer