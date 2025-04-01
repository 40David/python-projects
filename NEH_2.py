import numpy as np
import itertools
import matplotlib.pyplot as plt

def get_user_input():
    num_jobs = int(input("Enter number of jobs: "))
    jobs = []
    for i in range(num_jobs):
        job_id = input(f"Enter Job ID for job {i+1}: ")
        processing_times = list(map(int, input(f"Enter processing times for {job_id} on 5 machines (space-separated): ").split()))
        if len(processing_times) != 5:
            print("Error: Enter exactly 5 processing times.")
            return None
        jobs.append((job_id, processing_times))
    return jobs

def calculate_makespan(order, jobs):
    num_jobs = len(order)
    num_machines = 5
    schedule = np.zeros((num_jobs, num_machines))
    start_times = np.zeros((num_jobs, num_machines))
    
    for i, job_index in enumerate(order):
        processing_times = jobs[job_index][1]
        for j in range(num_machines):
            if i == 0 and j == 0:
                start_times[i][j] = 0
                schedule[i][j] = processing_times[j]
            elif j == 0:
                start_times[i][j] = schedule[i-1][j]
                schedule[i][j] = schedule[i-1][j] + processing_times[j]
            else:
                start_times[i][j] = max(schedule[i-1][j], schedule[i][j-1])
                schedule[i][j] = start_times[i][j] + processing_times[j]
    
    idle_time = np.sum(schedule) - np.sum([sum(jobs[i][1]) for i in order])
    total_elapsed_time = schedule[-1][-1]
    
    return schedule[-1][-1], start_times, schedule, idle_time, total_elapsed_time

def neh_algorithm(jobs):
    num_jobs = len(jobs)
    
    sorted_jobs = sorted(range(num_jobs), key=lambda x: sum(jobs[x][1]), reverse=True)
    sequence = [sorted_jobs[0]]
    
    for i in range(1, num_jobs):
        best_sequence = None
        best_makespan = float('inf')
        
        for position in range(i + 1):
            new_sequence = sequence[:position] + [sorted_jobs[i]] + sequence[position:]
            makespan, _, _, _, _ = calculate_makespan(new_sequence, jobs)
            
            if makespan < best_makespan:
                best_makespan = makespan
                best_sequence = new_sequence
        
        sequence = best_sequence  
    
    return sequence, *calculate_makespan(sequence, jobs)

def print_schedule_table(jobs, sequence, start_times, end_times):
    print("\nJob Schedule Table:")
    print("Job ID | Machine 1 (Start-End) | Machine 2 (Start-End) | Machine 3 (Start-End) | Machine 4 (Start-End) | Machine 5 (Start-End)")
    print("-" * 90)
    
    for i, job_index in enumerate(sequence):
        job_id = jobs[job_index][0]
        times = [f"{int(start_times[i][j])}-{int(end_times[i][j])}" for j in range(5)]
        print(f"{job_id:<6} | {times[0]:<20} | {times[1]:<20} | {times[2]:<20} | {times[3]:<20} | {times[4]:<20}")

def plot_gantt_chart(jobs, sequence, start_times, end_times):
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = plt.cm.get_cmap("tab10", len(sequence))
    
    for i, job_index in enumerate(sequence):
        job_id = jobs[job_index][0]
        for j in range(5):
            ax.barh(j, end_times[i][j] - start_times[i][j], left=start_times[i][j], color=colors(i), edgecolor='black', label=f"{job_id}" if j == 0 else "")
    
    ax.set_yticks(range(5))
    ax.set_yticklabels([f"Machine {i+1}" for i in range(5)])
    ax.set_xlabel("Time")
    ax.set_ylabel("Machines")
    ax.set_title("Flow Shop Scheduling Gantt Chart (NEH Algorithm)")
    ax.legend()
    plt.show()

def main():
    jobs = get_user_input()
    if jobs is None:
        return
    
    sequence, best_makespan, start_times, end_times, idle_time, total_elapsed_time = neh_algorithm(jobs)
    print("\nOptimal Job Sequence (NEH Heuristic):", [jobs[i][0] for i in sequence])
    print("Optimal Makespan:", best_makespan)
    print("Total Idle Time across all machines:", idle_time)
    print("Total Elapsed Time for all machines:", total_elapsed_time)
    
    print_schedule_table(jobs, sequence, start_times, end_times)
    plot_gantt_chart(jobs, sequence, start_times, end_times)

if __name__ == "__main__":
    main()
