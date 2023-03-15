class Task:
    name: str
    importance: int
    urgency: int
    priority: float

    def __init__(self, name: str, importance: int = None, urgency: int = None):
        self.name = name
        self.importance = importance
        self.urgency = urgency
        if self.importance and self.urgency:
            self.priority = (self.importance + self.urgency) / 2
        else:
            self.priority = None

    def __repr__(self):
        return f"{self.name}: " \
               f"\nImportance: {self.importance}" \
               f"\nUrgency: {self.urgency}" \
               f"\nTotal priority: {self.priority}"


class PositiveHabit(Task):
    pass

class NegativeHabit(Task):
    pass
