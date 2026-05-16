tasks = []

print("=== TO-DO LIST APP ===")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            remove_task = int(input("Enter task number to remove: "))

            if 1 <= remove_task <= len(tasks):
                removed = tasks.pop(remove_task - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting To-Do List...")
        break

    else:
        print("Invalid choice.")
