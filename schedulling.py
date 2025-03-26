from datetime import datetime, timedelta

class Job:
    def __init__(self, job_id, processing_time, due_date, setup_time=0):
        self.job_id = job_id
        self.processing_time = processing_time
        self.due_date = due_date
        self.setup_time = setup_time

    def __repr__(self):
        return (f"Job({self.job_id}, PT: {self.processing_time}, "
                f"DD: {self.due_date}, ST: {self.setup_time})")

def schedule_jobs(jobs, rule='SPT'):
    if rule == 'SPT':
        jobs.sort(key=lambda job: job.processing_time)
    elif rule == 'EDD':
        jobs.sort(key=lambda job: job.due_date)
    
    current_time = datetime.now()
    schedule = []
    total_tardiness = 0
    
    for job in jobs:
        start_time = current_time
        end_time = start_time + timedelta(minutes=job.processing_time + job.setup_time)
        tardiness = max(0, (end_time - job.due_date).total_seconds() / 60)
        total_tardiness += tardiness
        
        schedule.append((job.job_id, start_time, end_time, tardiness))
        current_time = end_time
    
    makespan = (schedule[-1][2] - schedule[0][1]).total_seconds() / 60
    
    return schedule, makespan, total_tardiness

def print_schedule(schedule):
    print("Schedule:")
    for job_id, start, end, tardiness in schedule:
        print(f"Job {job_id}: {start.strftime('%H:%M')} - {end.strftime('%H:%M')}, "
              f"Tardiness: {tardiness:.2f} minutes")
    
jobs = [
    Job("A", 30, datetime(2025, 3, 30, 12, 0), 5),
    Job("B", 20, datetime(2025, 3, 30, 11, 0), 3),
    Job("C", 25, datetime(2025, 3, 30, 10, 30), 2)
]

schedule, makespan, total_tardiness = schedule_jobs(jobs, rule='SPT')
print_schedule(schedule)
print("Makespan:", makespan, "minutes")
print("Total Tardiness:", total_tardiness, "minutes")