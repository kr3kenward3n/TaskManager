import json
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority, due_date):
        task = Task(description, priority, due_date)
        self.tasks.append(task)
        print(f"Задача добавлена: {task.description}")

    def remove_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            removed_task = self.tasks.pop(task_id)
            print(f"Задача удалена: {removed_task.description}")
        else:
            print("Некорректный идентификатор задачи.")

    def view_tasks(self, priority_filter=None):
        filtered_tasks = self.tasks
        if priority_filter:
            filtered_tasks = [task for task in self.tasks if task.priority == priority_filter]

        for idx, task in enumerate(filtered_tasks):
            print(f"{idx}: {task.description} | Приоритет: {task.priority} | Срок: {task.due_date}")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)
        print(f"Задачи сохранены в файл: {filename}")

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task.from_dict(task) for task in tasks_data]
            print(f"Задачи загружены из файла: {filename}")
        except FileNotFoundError:
            print("Файл не найден.")
        except json.JSONDecodeError:
            print("Ошибка при чтении файла.")