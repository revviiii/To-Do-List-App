tasks = []

def add_task(task):
    """Add a new task to the list"""
    tasks.append(task)
    print("Task added successfully!")

def show_tasks():
    """Display all tasks"""
    if len(tasks) == 0:
        print("No tasks added yet")
    else:
        for i in range (len(tasks)):
            print(i + 1, ".", tasks[i])
            
def remove_task(task_num):
    """Remove a task by its number"""
    if task_num < 1 or task_num > len(tasks):
        print("Invalid task number!")
    else:
        tasks.pop(task_num - 1) 
        print("Task removed successfully!")

def main():
    while True:

        print("--------------To-Do List Menu--------------")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            t = input("Enter your to-do task: ")
            add_task(t)

        elif choice =="2":
            show_tasks()

        elif choice =="3":
          try:
            n = int(input("Enter task number to remove: "))
            remove_task(n)
          except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice =="4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")
main()