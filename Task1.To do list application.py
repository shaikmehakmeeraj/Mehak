def display_menu():
    print("\nTo-Do List Application")
    print("1. Display To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Remove a Task")
    print("5. Quit")

def display_todo_list(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, (task, completed) in enumerate(todo_list, start=1):
            status = "Completed" if completed else "Not Completed"
            print(f"{index}. {task} - {status}")

def add_task(todo_list):
    task = input("\nEnter the task's name: ")
    todo_list.append((task, False))
    print(f"Task '{task}' added to the to-do list.")

def mark_task_completed(todo_list):
    display_todo_list(todo_list)
    if todo_list:
        try:
            task_number = int(input("\nEnter the task number you want to mark as completed: "))
            if 1 <= task_number <= len(todo_list):
                task, _ = todo_list[task_number - 1]
                todo_list[task_number - 1] = (task, True)
                print(f"Task '{task}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def remove_task(todo_list):
    display_todo_list(todo_list)
    if todo_list:
        try:
            task_number = int(input("\nEnter the task number you want to remove: "))
            if 1 <= task_number <= len(todo_list):
                task, _ = todo_list.pop(task_number - 1)
                print(f"Task '{task}' removed from the to-do list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    todo_list = []
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                display_todo_list(todo_list)
            elif choice == 2:
                add_task(todo_list)
            elif choice == 3:
                mark_task_completed(todo_list)
            elif choice == 4:
                remove_task(todo_list)
            elif choice == 5:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
