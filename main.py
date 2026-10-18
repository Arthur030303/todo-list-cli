# To-Do List (CLI)

print("To-Do List\n")

while True:
    print("1. Add Task\n2. View Task\n3. Quit")
    choice = input("Choose(1,2,3): ")
    if choice == "1":
        print("==Add Task==")
    elif choice == "2":
        print("==View Task==")
    elif choice == "3":
        print("You have exited.")
        break
    else:
        print("Invalid Choice, Please Select again.")
    