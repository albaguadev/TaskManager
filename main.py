from task_manager import TaskManager
from ai_service import create_simple_tasks

def print_menu():
    print("\n--- Task Manager ---\n")
    print("1. Add Task")
    print("2. Add complex Task (with AI)")
    print("3. Delete Task")
    print("4. Complete Task")
    print("5. List Tasks")
    print("6. Exit")

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
          description = input("Enter complex task description: ")
          subtasks = create_simple_tasks(description)
          for subtask in subtasks:
            if not subtask.startswith("Error:"):
              task_manager.add_task(subtask)
            else:
              print(subtask)
              break
        case 3:
          id = int(input("Enter task ID to delete: "))
          task_manager.delete_task(id)
        case 4:
          id = int(input("Enter task ID to complete: "))
          task_manager.complete_task(id)
        case 5:
          task_manager.list_tasks()
        case 6:
          print("Exiting Task Manager. Goodbye!")
          break
        case _:
          print("Invalid option. Please try again.")

    except ValueError:
      print("Invalid option. Please try again.")
  

if __name__ == "__main__":
  main()