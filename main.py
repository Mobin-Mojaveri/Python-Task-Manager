
from task_manager import (
    add_task,
    show_tasks,
    delete_task,
    update_task,
    complete_task,
    search_tasks
)




def main():
    while True:
        print("\n========== TASK MANAGER ==========")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Complete Task")
        print("6. Search Task")
        print("7. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            show_tasks()
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            show_tasks()
            try:
                task_id = int(input("Enter task ID: "))
                new_title = input("Enter new title: ")
                update_task(task_id, new_title)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            show_tasks()
            try:
                task_id = int(input("Enter task ID to complete: "))
                complete_task(task_id)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "6":
            keyword = input("Enter search keyword: ")
            search_tasks(keyword)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

