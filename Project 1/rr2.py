from collections import deque
import copy

def RR2(jobs):
    jobs = copy.deepcopy(jobs)
    turnaround_time = 0
    current_time = 0
    results = []
    queue = deque(jobs)
    while queue:
        job = queue.popleft()
        if job.length > 2:
            current_time += 2
            job.length -= 2
            results.append((job.name, current_time - 2, current_time, False))
            queue.append(job)
        else:
            current_time += job.length
            results.append((job.name, current_time - job.length, current_time, True))
            turnaround_time += current_time

    return results, turnaround_time/len(jobs)