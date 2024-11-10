from datetime import datetime

class Task:
    def __init__(self, description, priority, due_date):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date.strftime('%Y-%m-%d'),
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    @classmethod
    def from_dict(cls, data):
        due_date = datetime.strptime(data['due_date'], '%Y-%m-%d')
        return cls(data['description'], data['priority'], due_date)