from src.models import Task


def collect_tasks_from_terminal() -> list[Task]:
    task_name: str = input("Name of new task: ")
    yield Task(task_name)
