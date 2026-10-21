# To-Do List (CLI)

print("To-Do List\n")
tasks = []
while True:
    print("\n1. Add Task\n2. View Task\n3. Quit")
    choice = input("\nChoose(1,2,3): ")
    if choice == "1":
        print("\n==Add Task==")
        task = input("Enter the task: ")
        tasks.append(task)
    elif choice == "2":
        print("\n==View Task==")
        if not tasks:
            print("There is no task.")
        else: 
            for index, task in enumerate(tasks, start = 1):
                print(f"{index}. {task}")
    elif choice == "3":
        print("\nYou have exited.")
        break
    else:
        print("\nInvalid Choice, Please Select again.")
