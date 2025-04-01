import numpy as np
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

def flow_shop_schedule(jobs):
    num_jobs = len(jobs)
    num_machines = 5
    schedule = np.zeros((num_jobs, num_machines))
    start_times = np.zeros((num_jobs, num_machines))
    
    # Fill schedule matrix with processing times and calculate start times
    for i, (job_id, processing_times) in enumerate(jobs):
        for j in range(num_machines):
            if i == 0 and j == 0:
                start_times[i][j] = 0
                schedule[i][j] = processing_times[j]
            elif j == 0:
                start_times[i][j] = schedule[i-1][j]
                schedule[i][j] = start_times[i][j] + processing_times[j]
            else:
                start_times[i][j] = max(schedule[i-1][j], schedule[i][j-1])
                schedule[i][j] = start_times[i][j] + processing_times[j]
    
    return schedule, start_times

def calculate_idle_times(schedule, jobs):
    num_machines = 5
    idle_times = np.zeros(num_machines)
    
    for j in range(num_machines):
        last_end_time = 0
        for i in range(len(jobs)):
            idle_times[j] += max(0, schedule[i][j] - last_end_time - jobs[i][1][j])
            last_end_time = schedule[i][j]
    
    return idle_times

def plot_gantt_chart(jobs, schedule, start_times):
    num_jobs = len(jobs)
    num_machines = 5
    machine_labels = [f"Machine {i+1}" for i in range(num_machines)]
    colors = plt.cm.get_cmap("tab10", num_jobs)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for i, (job_id, _) in enumerate(jobs):
        for j in range(num_machines):
            start_time = start_times[i][j]
            end_time = schedule[i][j]
            ax.barh(j, end_time - start_time, left=start_time, color=colors(i), edgecolor='black', label=f"{job_id}" if j == 0 else "")
    
    ax.set_yticks(range(num_machines))
    ax.set_yticklabels(machine_labels)
    ax.set_xlabel("Time")
    ax.set_ylabel("Machines")
    ax.set_title("Flow Shop Scheduling Gantt Chart")
    ax.legend()
    plt.show()

def main():
    jobs = get_user_input()
    if jobs is None:
        return
    
    schedule, start_times = flow_shop_schedule(jobs)
    idle_times = calculate_idle_times(schedule, jobs)
    
    print("\nJob Sequence:")
    for job in jobs:
        print(job[0], end=' -> ')
    print("End")
    
    print("\nIdle Times for Machines:")
    for i, idle_time in enumerate(idle_times):
        print(f"Machine {i+1}: {idle_time} time units")
    
    print("\nStart Time and End Time Table:")
    print("Job | Machine 1 | Machine 2 | Machine 3 | Machine 4 | Machine 5")
    print("---------------------------------------------------------------")
    for i, (job_id, _) in enumerate(jobs):
        row = f"{job_id}  | "
        row += " | ".join([f"{int(start_times[i][j])}-{int(schedule[i][j])}" for j in range(5)])
        print(row)
    
    plot_gantt_chart(jobs, schedule, start_times)

if __name__ == "__main__":
    main()