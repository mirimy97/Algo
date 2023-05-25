def solution(jobs):
    # jobs = [[0, 3], [1, 9], [2, 6]]
    
    total_time = 0
    min_start = 1001
    for i in range(len(jobs)):
        if jobs[i][0] < min_start:
            min_start = jobs[i][0]
    start = min_start
    len_jobs = len(jobs)
    
    while jobs:
    
        min_job = [0, 1001]   # [인덱스, 시간]
        for i in range(len(jobs)):
            
            if jobs[i][0] <= start and jobs[i][1] < min_job[1]:
                min_job = [i, jobs[i][1]]

        if min_job[1] != 1001:
            total_time += (start - jobs.pop(min_job[0])[0]) + min_job[1]
            start += min_job[1]
        else:
            min_start = 1001
            for i in range(len(jobs)):
                if jobs[i][0] < min_start:
                    min_start = jobs[i][0]
            start = min_start 

    answer = int(total_time / len_jobs)
    
    return answer