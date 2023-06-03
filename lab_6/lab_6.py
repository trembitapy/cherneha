import math

class Task:
    def __init__(self, a, m, b):
        self.a = a
        self.m = m
        self.b = b

    def calculate_estimation(self):
        E = (self.a + 4 * self.m + self.b) / 6
        SD = (self.b - self.a) / 6
        return E, SD

class Project:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def calculate_estimation(self):
        E_project = sum(task.calculate_estimation()[0] for task in self.tasks)
        SD_project = math.sqrt(sum(task.calculate_estimation()[1]**2 for task in self.tasks))
        return E_project, SD_project

    def calculate_confidence_interval(self, E_project, SD_project):
        CI_min = E_project - 2 * SD_project
        CI_max = E_project + 2 * SD_project
        return CI_min, CI_max

def main():
    project = Project()

    while True:
        try:
            a = float(input("Enter the optimistic estimate (a) for a task (or enter 'q' to quit): "))
        except ValueError:
            break
        m = float(input("Enter the most likely estimate (m) for the task: "))
        b = float(input("Enter the pessimistic estimate (b) for the task: "))

        task = Task(a, m, b)
        project.add_task(task)

    E_project, SD_project = project.calculate_estimation()
    CI_min, CI_max = project.calculate_confidence_interval(E_project, SD_project)

    print(f"Project's 95% confidence interval: {CI_min} ... {CI_max} points")

if __name__ == '__main__':
    main()
