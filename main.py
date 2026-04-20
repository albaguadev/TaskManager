from task_manager import TaskManager

def print_menu():
    print("\n--- Task Manager ---\n")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Complete Task")
    print("4. List Tasks")
    print("5. Exit")

def main():

  task_manager = TaskManager()

  while True:

    print_menu()

    try:  
      choice = int(input("Choose an option: "))

      match choice:
        case 1:
          description = input("Enter task description: ")
          task_manager.add_task(description)
        case 2 :
          id = int(input("Enter task ID to delete: "))
          task_manager.delete_task(id)
        case 3:
          id = int(input("Enter task ID to complete: "))
          task_manager.complete_task(id)
        case 4:
          task_manager.list_tasks()
        case 5:
          print("Exiting Task Manager. Goodbye!")
          break
        case _:
          print("Invalid option. Please try again.")

    except ValueError:
      print("Invalid option. Please try again.")
  

if __name__ == "__main__":
  main()