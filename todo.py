# todo.py

FILE_NAME = "tasks.txt"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            tasks = [line.strip() for line in f.readlines() if line.strip()]
        return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Task cannot be empty.")


def remove_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    choice = input("Enter task number to remove: ").strip()
    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    index = int(choice) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Removed: {removed}")
    else:
        print("Task number out of range.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Quit")

        option = input("Choose an option (1-4): ").strip()

        if option == "1":
            show_tasks(tasks)
        elif option == "2":
            add_task(tasks)
        elif option == "3":
            remove_task(tasks)
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
