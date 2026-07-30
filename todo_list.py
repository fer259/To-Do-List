tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter Task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == "2":
        if not tasks:
            print("No Tasks Found!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        task = input("Enter Task to Remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task Removed Successfully!")
        else:
            print("Task Not Found!")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
