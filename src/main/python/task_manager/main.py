from datetime import datetime
from task_manager import TaskManager
from utils import parse_date


def main():
    manager = TaskManager()

    while True:
        print("\nДоступные команды:")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Просмотреть задачи")
        print("4. Сохранить задачи в файл")
        print("5. Загрузить задачи из файла")
        print("6. Выход")

        choice = input("Выберите команду (1-6): ")

        if choice == '1':
            description = input("Введите описание задачи: ")
            priority = input("Введите приоритет (Высокий/Средний/Низкий): ")
            due_date_str = input("Введите срок выполнения (YYYY-MM-DD): ")
            due_date = parse_date(due_date_str)
            manager.add_task(description, priority, due_date)

        elif choice == '2':
            task_id = int(input("Введите идентификатор задачи для удаления: "))
            manager.remove_task(task_id)

        elif choice == '3':
            priority_filter = input("Введите приоритет для фильтрации (или оставьте пустым): ")
            manager.view_tasks(priority_filter if priority_filter else None)

        elif choice == '4':
            filename = input("Введите имя файла для сохранения задач: ")
            manager.save_tasks(filename)

        elif choice == '5':
            filename = input("Введите имя файла для загрузки задач: ")
            manager.load_tasks(filename)

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, выберите команду от 1 до 6.")


if __name__ == "__main__":
    main()