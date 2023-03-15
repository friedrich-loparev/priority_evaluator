from src.models import Task
from task_collector import collect_tasks_from_terminal


tasks: list[Task] = collect_tasks_from_terminal()
for task in tasks:
    print(task)
