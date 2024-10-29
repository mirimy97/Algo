import math

def solution(progresses, speeds):
    answer = []
    time = []
    cnt = 0
    for i in range(0, len(speeds)):
        num = math.ceil((100 - progresses[i]) / speeds[i])
        if not time or time[-1][0] < num:
            cnt = 1
            time.append([num, cnt])
        else:
            time[-1][1] += 1
    for t in time:
        answer.append(t[1])
    return answer