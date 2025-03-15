import os

FILE_NAME = "tasks.txt"

# Function to load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [task.strip() for task in file.readlines()]
    return []

# Function to save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Main program
tasks = load_tasks()

while True:
    print("\n📝 To-Do List Manager")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if not tasks:
            print("No tasks found.")
        else:
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added!")

    elif choice == "3":
        task_number = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Exiting To-Do List Manager.")
        break

    else:
        print("Invalid choice! Please try again.")
