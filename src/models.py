class Task:
    name: str
    importance: int
    urgency: int
    priority: float

    def __init__(self, name: str, importance: int = None, urgency: int = None, priority: float = None):
        self.name = name
        self.importance = importance
        self.urgency = urgency
        self.priority = (self.importance + self.urgency) / 2

    def __repr__(self):
        return f"{self.name}: " \
               f"\nImportance: {self.importance}" \
               f"\nUrgency: {self.urgency}" \
               f"\nTotal priority: {self.priority}"


task_1 = Task("Task 1", 5, 8)
print(task_1)
