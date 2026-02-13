import os
import random
from tabulate import tabulate
from matplotlib import pyplot as plt
from fcfs import FCFS
from sjf import SJF
from rr2 import RR2
from rr5 import RR5

class Job:
    def __init__(self, name, length):
        self.name = name
        self.length = length

def parse_file(filename):
    dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(dir, filename)
    jobs = []
    with open(filepath, 'r') as file:
        lines = file.read().strip().split('\n')
        for i in range(0, len(lines), 2):
            name = lines[i]
            length = int(lines[i + 1])
            jobs.append(Job(name, length))
    return jobs

# results can be stored in this format: [(job_name, start_time, end_time, completed), ...]
def print_table(results):
    headers = ["Job#", "Start Time", "End Time", "Job Completion"]
    formatted_results = []
    for job_name, start_time, end_time, completed in results:
        completion_status = f"{job_name} completed @{end_time}" if completed else ""
        formatted_results.append((job_name, start_time, end_time, completion_status))
    print(tabulate(formatted_results, headers, tablefmt="grid"))

# this will overwrite the job.txt
def generate_new_jobs(size):
    with open("job.txt", "w") as f:
        for i in range(1, size + 1):
            length = random.randint(1, 20)
            f.write(f"Job{i}\n")
            f.write(f"{length}\n")


def main():
    # Part 1 and 2 - used a generator to genereate the files
    print("PART 1 and 2 - testing algorithmns with 5, 10, and 15 jobs")
    first_test_job = parse_file("5_jobs.txt")
    second_test_job = parse_file("10_jobs.txt")
    third_test_job = parse_file("15_jobs.txt")

    # First Come First Serve Algo
    print("----- FCFS -----")
    print("5 test job:")
    results, turnaround_time = FCFS(first_test_job)
    print_table(results)
    print(f"Average Turnaround Time: {turnaround_time:.2f}\n")

    print("10 test job:")
    results, turnaround_time = FCFS(second_test_job)
    print_table(results)
    print(f"Average Turnaround Time: {turnaround_time:.2f}\n")

    print("15 test job:")
    results, turnaround_time = FCFS(third_test_job)
    print_table(results)
    print(f"Average Turnaround Time: {turnaround_time:.2f}\n")

    # Shortest Job First Algo
    print("-----  SJF 5 -----")
    print("5 test job:")
    results, turnaround_time = SJF(first_test_job)
    print_table(results)
    print(f"Average Turnaround Time: {turnaround_time:.2f}\n")

    print("10 test job:")
    results, turnaround_time = SJF(second_test_job)
    print_table(results)
    print(f"Average Turnaround Time: {turnaround_time:.2f}\n")

    print("15 test job:")
    results, turnaround_time = SJF(third_test_job) 
    print_table(results)
    print(f"Average Turnaround Time: {turnaround_time:.2f}\n")

    # Round Robin with Quantum Slice 2
    print("----- RR2 -----")
    print("5 test job:")
    results, turnaround_time = RR2(first_test_job)
    print_table(results)
    print(f"Average Turnaround Time: {turnaround_time:.2f}\n")

    print("10 test job:")
    results, turnaround_time = RR2(second_test_job)
    print_table(results)
    print(f"Average Turnaround Time: {turnaround_time:.2f}\n")

    print("15 test job:")
    results, turnaround_time = RR2(third_test_job)
    print_table(results)
    print(f"Average Turnaround Time: {turnaround_time:.2f}\n")

    # Round Robin with Quantum Slice 5
    print("----- RR5 -----")
    print("5 test job:")
    results, turnaround_time = RR5(first_test_job)
    print_table(results)
    print(f"Average Turnaround Time: {turnaround_time:.2f}\n")

    print("10 test job:")
    results, turnaround_time = RR5(second_test_job)
    print_table(results)
    print(f"Average Turnaround Time: {turnaround_time:.2f}\n")

    print("15 test job:")
    results, turnaround_time = RR5(third_test_job)
    print_table(results)
    print(f"Average Turnaround Time: {turnaround_time:.2f}\n")

    # Part 3
    print("PART 3 - Calculating average turnaround times")
    # Dictionary mapping name to their function
    algorithms = {
        'FCFS': FCFS,
        'SJF': SJF,
        'RR2': RR2,
        'RR5': RR5
    }

    # Total to get average later
    totals = {name: 0 for name in algorithms}

    # 5 jobs results
    for i in range(20):
        generate_new_jobs(5)
        jobs = parse_file("job.txt")
        
        # Run all algorithms and accumulate their average turnaround times
        for name, func in algorithms.items():
            _, turnaround = func(jobs)
            totals[name] += turnaround
    
    # Calculate and display overall averages
    print(f"\nAverage Turnaround Times for 5 jobs: ")
    for name, total in totals.items():
        totals[name] = total / 20
        print(f"{name}: {totals[name]:.2f}")
    
    # Reset
    totals = {name: 0 for name in algorithms}
    
    # 10 jobs results
    for i in range(20):
        generate_new_jobs(10)
        jobs = parse_file("job.txt")
    
        for name, func in algorithms.items():
            _, turnaround = func(jobs)
            totals[name] += turnaround
    
    print(f"\nAverage Turnaround Times for 10 jobs: ")
    for name, total in totals.items():
        average = total / 20
        print(f"{name}: {average:.2f}")
    
    # Reset
    totals = {name: 0 for name in algorithms}
    
    # 15 jobs results
    for i in range(20):
        generate_new_jobs(15)
        jobs = parse_file("job.txt")
        
        for name, func in algorithms.items():
            _, turnaround = func(jobs)
            totals[name] += turnaround
    
    print(f"\nAverage Turnaround Times for 15 jobs: ")
    for name, total in totals.items():
        average = total / 20
        print(f"{name}: {average:.2f}")


    # This is for graphing portion- part 3b
    results = {name: [] for name in algorithms}
    for i in range(1, 31):
        totals = {name: 0 for name in algorithms}
        for _ in range(20):
            generate_new_jobs(i)
            jobs = parse_file("job.txt")
            for name, func in algorithms.items():
                _, turnaround = func(jobs)
                totals[name] += turnaround
        for name in algorithms:
            results[name].append(totals[name] / 20)
        
    xPoints = list(range(1, 31))
    for name, values in results.items():
        plt.figure()
        plt.plot(xPoints, values, label=name)
        plt.xlabel("Number of Jobs")
        plt.ylabel("Average Turnaround Time")
        plt.title(f"{name} Algorithmn Turnaround Time(ms) vs Job Size")
        plt.legend()
        plt.show()

    # All together in one
    plt.figure()
    for name, values in results.items():
        plt.plot(xPoints, values, label=name)
    plt.xlabel("Number of Jobs")
    plt.ylabel("Average Turnaround Time")
    plt.title("Algorithm Comparison by Job Size")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()