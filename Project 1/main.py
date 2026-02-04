import os

def parse_file(filename):
    dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(dir, filename)
    jobs = []
    with open(filepath, 'r') as file:
        lines = file.read().strip().split('\n')
        for i in range(0, len(lines), 2):
            job_name = lines[i]
            job_time = int(lines[i + 1])
            jobs.append((job_name, job_time))
    return jobs

def FCFS(jobs):
    pass

def SJF(jobs):
    pass

def RR2(jobs):
    pass

def RR5(jobs):
    pass



def main():
    jobs = parse_file("5_jobs.txt")
    for job_name, job_time in jobs:
        print(f"{job_name}: {job_time}ms")
    pass

if __name__ == "__main__":
    main()