import os

class Task:
    def __init__(self, task_id, description, due_date):
        self.task_id = task_id
        self.description = description
        self.due_date = due_date

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task_id = len(self.tasks) + 1
        task = Task(task_id, description, due_date)
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(f"Task ID: {task.task_id}, Description: {task.description}, Due Date: {task.due_date}")

    def update_task(self, task_id, new_description, new_due_date):
        task = self.find_task(task_id)
        if task:
            task.description = new_description
            task.due_date = new_due_date
            print("Task updated successfully!")
        else:
            print("Task not found.")

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            print("Task deleted successfully!")
        else:
            print("Task not found.")

    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            clear_screen()
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            task_manager.add_task(description, due_date)

        elif choice == "2":
            clear_screen()
            task_manager.view_tasks()

        elif choice == "3":
            clear_screen()
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new task description: ")
            new_due_date = input("Enter new due date: ")
            task_manager.update_task(task_id, new_description, new_due_date)

        elif choice == "4":
            clear_screen()
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)

        elif choice == "5":
            clear_screen()
            print("Goodbye!")
            break

        else:
            clear_screen()
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
