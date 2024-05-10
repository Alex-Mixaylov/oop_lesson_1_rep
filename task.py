# Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def __str__(self):
        return (f"Задача: {self.description}, Срок завершения: {self.due_date}, Статус завершения: {self.is_completed}")


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        self.tasks.append(Task(description, due_date))

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
            return True
        return False

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.is_completed]


def main_menu():
    task_manager = TaskManager()
    while True:
        print("\nМеню Таск Менеджера:")
        print("1. Добавить Задачу")
        print("2. Отметить задачу как завершенную")
        print("3. Показать список текущих задач")
        print("4. Выход")
        choice = input("Выберите опцию: ")

        if choice == '1':
            description = input("Введите описание задачи: ")
            due_date = input("Введите дату завершения задачи в формате (ГГГГ-MM-ДД): ")
            task_manager.add_task(description, due_date)
            print("Задача добавлена")

        elif choice == '2':
            if task_manager.tasks:
                for index, task in enumerate(task_manager.tasks):
                    print(f"{index}: {task}")
                task_index = int(input("Введите номер (индекс) задачи, которая завершена: "))
                if task_manager.mark_task_completed(task_index):
                    print("Задача отмечена как завершенная.")
                else:
                    print("Некорректный номер индекс задачи.")
            else:
                print("Нет задачи для отметки как завершенной.")

        elif choice == '3':
            current_tasks = task_manager.get_current_tasks()
            if current_tasks:
                for task in current_tasks:
                    print(task)
            else:
                print("Нет текущих задач.")

        elif choice == '4':
            print("Выйти из программы")
            break

        else:
            print("Некорректный выбор. Выберите еще раз.")

if __name__ == "__main__":
    main_menu()
