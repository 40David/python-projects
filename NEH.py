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
    
    for i, job_index in enumerate(order):
        processing_times = jobs[job_index][1]
        for j in range(num_machines):
            if i == 0 and j == 0:
                schedule[i][j] = processing_times[j]
            elif j == 0:
                schedule[i][j] = schedule[i-1][j] + processing_times[j]
            else:
                schedule[i][j] = max(schedule[i-1][j], schedule[i][j-1]) + processing_times[j]
    
    return schedule[-1][-1]  # Makespan is the last job's completion time on the last machine

def neh_algorithm(jobs):
    num_jobs = len(jobs)
    
    # Step 1: Sort jobs by total processing time in descending order
    sorted_jobs = sorted(range(num_jobs), key=lambda x: sum(jobs[x][1]), reverse=True)
    
    # Step 2: Initialize sequence with first job
    sequence = [sorted_jobs[0]]
    
    # Step 3: Iteratively insert jobs in the best position
    for i in range(1, num_jobs):
        best_sequence = None
        best_makespan = float('inf')
        
        for position in range(i + 1):
            new_sequence = sequence[:position] + [sorted_jobs[i]] + sequence[position:]
            makespan = calculate_makespan(new_sequence, jobs)
            
            if makespan < best_makespan:
                best_makespan = makespan
                best_sequence = new_sequence
        
        sequence = best_sequence  # Update sequence with best insertion order
    
    return sequence, calculate_makespan(sequence, jobs)

def plot_gantt_chart(jobs, sequence):
    num_jobs = len(sequence)
    num_machines = 5
    schedule = np.zeros((num_jobs, num_machines))
    
    for i, job_index in enumerate(sequence):
        processing_times = jobs[job_index][1]
        for j in range(num_machines):
            if i == 0 and j == 0:
                schedule[i][j] = processing_times[j]
            elif j == 0:
                schedule[i][j] = schedule[i-1][j] + processing_times[j]
            else:
                schedule[i][j] = max(schedule[i-1][j], schedule[i][j-1]) + processing_times[j]
    
    machine_labels = [f"Machine {i+1}" for i in range(num_machines)]
    colors = plt.cm.get_cmap("tab10", num_jobs)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for i, job_index in enumerate(sequence):
        job_id = jobs[job_index][0]
        for j in range(num_machines):
            start_time = 0 if j == 0 else schedule[i][j-1]
            end_time = schedule[i][j]
            ax.barh(j, end_time - start_time, left=start_time, color=colors(i), edgecolor='black', label=f"{job_id}" if j == 0 else "")
    
    ax.set_yticks(range(num_machines))
    ax.set_yticklabels(machine_labels)
    ax.set_xlabel("Time")
    ax.set_ylabel("Machines")
    ax.set_title("Flow Shop Scheduling Gantt Chart (NEH Algorithm)")
    ax.legend()
    plt.show()

def main():
    jobs = get_user_input()
    if jobs is None:
        return
    
    sequence, best_makespan = neh_algorithm(jobs)
    print("\nOptimal Job Sequence (NEH Heuristic):", [jobs[i][0] for i in sequence])
    print("Optimal Makespan:", best_makespan)
    
    plot_gantt_chart(jobs, sequence)

if __name__ == "__main__":
    main()