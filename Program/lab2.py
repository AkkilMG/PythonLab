class Job:
    def __init__(self, taskId, deadline, profit):
        self.taskId = taskId
        self.deadline = deadline
        self.profit = profit

def schedulejobs(jobs, T):
    profit=0
    slot=[-1]*T
    jobs.sort(key=lambda x: x.profit, reverse=True)
    for job in jobs:
        for j in reversed(range(min(T, job.deadline))):
            if slot[j]==-1:
                slot[j]=job.taskId
                profit += job.profit
                break 
    print("The scheduled jobs are",list(filter(lambda x: x !=-1,slot)))
    print("The total profit earned is",profit) 

if __name__ =='__main__':   
    n = int(input("Enter the number of jobs: "))
    jobs = []
    for i in range(n):
        taskId = input("Enter task ID for job {}: ".format(i+1))
        deadline = int(input("Enter deadline for job {}: ".format(i+1)))
        profit = int(input("Enter profit for job {}: ".format(i+1)))
        jobs.append(Job(taskId, deadline, profit))
    T = int(input("Enter the total time: "))
    schedulejobs(jobs, T)