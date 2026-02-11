# Pre-sorting first
import copy

def SJF(jobs):
    jobs = copy.deepcopy(jobs)
    turnaround_time = 0
    current_time = 0
    results = []
    jobs_sorted = sorted(jobs, key=lambda x: x.length)
    for job in jobs_sorted:
        results.append((job.name, current_time, current_time + job.length, True))
        current_time += job.length
        turnaround_time += current_time

    return results, turnaround_time/len(jobs)