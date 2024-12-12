import getpass

def login():
  """
  This function handles the login process.
  """
  username = input("Username: ")
  password = getpass.getpass("Password: ")

  # Replace this with your actual authentication logic
  if username == "admin" and password == "batstate":
    print("Login successful!")
    return True
  else:
    print("Invalid username or password.")
    return False

def todo_list():
  """
  This function manages the to-do list.
  """
  tasks = []
  while True:
    print("\nChoose an option:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      task = input("Enter task: ")
      tasks.append(task)
      print("Task added successfully!")
    elif choice == '2':
      if tasks:
        for i, task in enumerate(tasks):
          print(f"{i+1}. {task}")
      else:
        print("No tasks yet.")
    elif choice == '3':
      if tasks:
        for i, task in enumerate(tasks):
          print(f"{i+1}. {task}")
        index = int(input("Enter the number of the task to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
          tasks[index] = f"~~{tasks[index]}~~"
          print("Task marked as completed.")
        else:
          print("Invalid task number.")
      else:
        print("No tasks to mark as completed.")
    elif choice == '4':
      if tasks:
        for i, task in enumerate(tasks):
          print(f"{i+1}. {task}")
        index = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= index < len(tasks):
          del tasks[index]
          print("Task deleted.")
        else:
          print("Invalid task number.")
      else:
        print("No tasks to delete.")
    elif choice == '5':
      print("Exiting...")
      break
    else:
      print("Invalid choice.")

if __name__ == "__main__":
  if login():
    todo_list()