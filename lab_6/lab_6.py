import math

def calculate_task_estimation(a, m, b):
    E_task = (a + 4 * m + b) / 6
    SD_task = (b - a) / 6
    return E_task, SD_task

def calculate_project_estimation(tasks):
    E_project = sum(task[0] for task in tasks)
    SD_project = math.sqrt(sum(task[1]**2 for task in tasks))
    return E_project, SD_project

def calculate_confidence_interval(E_project, SD_project):
    CI_min = E_project - 2 * SD_project
    CI_max = E_project + 2 * SD_project
    return CI_min, CI_max

def main():
    tasks = []
    while True:
        try:
            a = float(input("Enter the optimistic estimate (a) for a task (or enter 'q' to quit): "))
        except ValueError:
            break
        m = float(input("Enter the most likely estimate (m) for the task: "))
        b = float(input("Enter the pessimistic estimate (b) for the task: "))

        E_task, SD_task = calculate_task_estimation(a, m, b)
        tasks.append((E_task, SD_task))

    E_project, SD_project = calculate_project_estimation(tasks)
    CI_min, CI_max = calculate_confidence_interval(E_project, SD_project)

    print(f"Project's 95% confidence interval: {CI_min} ... {CI_max} points")

if __name__ == '__main__':
    main()