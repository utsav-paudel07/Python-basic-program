import json

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, description, deadline):
        task = {"description": description, "deadline": deadline, "completed": False}
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['description']} (Deadline: {task['deadline']}) - {status}")

    def complete_task(self, task_number):
        try:
            self.tasks[task_number - 1]["completed"] = True
            self.save_tasks()
            print("Task marked as completed.")
        except IndexError:
            print("Invalid task number.")

def menu():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            deadline = input("Enter task deadline: ")
            task_manager.add_task(description, deadline)
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_manager.view_tasks()
            task_number = int(input("Enter task number to complete: "))
            task_manager.complete_task(task_number)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
