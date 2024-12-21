def main():
    tasks = load_tasks_from_file()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Save & Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter priority (low, medium, high): ")
            add_task(tasks, title, description, priority)
        elif choice == '2':
            title = input("Enter task title to remove: ")
            tasks = remove_task(tasks, title)
        elif choice == '3':
            title = input("Enter task title to mark as completed: ")
            mark_completed(tasks, title)
        elif choice == '4':
            list_tasks(tasks)
        elif choice == '5':
            save_tasks_to_file(tasks)
            print("Tasks saved successfully. Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
