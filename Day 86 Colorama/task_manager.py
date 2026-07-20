from colorama import init, Fore, Style

init(autoreset=True)

tasks = []


def add_task():
    task = input("Enter Task: ").strip()

    if task:
        tasks.append({"task": task, "done": False})
        print(Fore.GREEN + "✔ Task added successfully!")
    else:
        print(Fore.RED + "Task cannot be empty.")


def view_tasks():
    if not tasks:
        print(Fore.YELLOW + "\nNo tasks available.")
        return

    print("\nYour Tasks")
    print("-" * 35)

    for index, task in enumerate(tasks, start=1):
        if task["done"]:
            print(Fore.GREEN + f"{index}. ✔ {task['task']}")
        else:
            print(Fore.RED + f"{index}. ✘ {task['task']}")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        choice = int(input("\nEnter task number: "))

        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            print(Fore.CYAN + "Task marked as completed!")
        else:
            print(Fore.RED + "Invalid task number.")
    except ValueError:
        print(Fore.RED + "Please enter a valid number.")


def main():

    while True:

        print(Style.BRIGHT + "\n====== TASK MANAGER ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            print(Fore.MAGENTA + "\nGoodbye!")
            break

        else:
            print(Fore.RED + "Invalid choice.")


if __name__ == "__main__":
    main()