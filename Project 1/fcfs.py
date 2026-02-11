import copy

def FCFS(jobs):
    jobs = copy.deepcopy(jobs)
    turnaround_time = 0
    current_time = 0
    results = []
    for job in jobs:
        results.append((job.name, current_time, current_time + job.length, True))
        current_time += job.length
        turnaround_time += current_time
    return results, turnaround_time/len(jobs)
