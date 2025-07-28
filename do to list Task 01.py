def simple_to_do():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose (1-5): ").strip()

        if choice == '1':
            name = input("Enter a task: ").strip()
            if name:
                tasks.append({"name": name, "done": False})
                print("Task added.")
            else:
                print("Task can't be empty.")

        elif choice == '2':
            if not tasks:
                print("No tasks yet.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    mark = "✅" if task["done"] else "❌"
                    print(f"{i}. {task['name']} [{mark}]")

        elif choice == '3':
            if not tasks:
                print("No tasks to mark.")
                continue
            num = input("Task number to mark as done: ")
            if num.isdigit():
                idx = int(num) - 1
                if 0 <= idx < len(tasks):
                    if not tasks[idx]["done"]:
                        tasks[idx]["done"] = True
                        print("Task marked as done.")
                    else:
                        print("Already done.")
                else:
                    print("Wrong task number.")
            else:
                print("Please type a number.")

        elif choice == '4':
            if not tasks:
                print("No tasks to delete.")
                continue
            num = input("Task number to delete: ")
            if num.isdigit():
                idx = int(num) - 1
                if 0 <= idx < len(tasks):
                    removed = tasks.pop(idx)
                    print(f"Deleted: {removed['name']}")
                else:
                    print("Invalid number.")
            else:
                print("Please enter a number.")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Choose a number from 1 to 5.")

simple_to_do()
