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
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4- Exit")
        ch = input("enter choice : ")
        if ch=="1":
            t = input("enter task : ")
            add_task(t)
        elif ch=="2":
            show_tasks()
        elif ch=="3":
            n=int(input("enter task no to remove: "))
            remove_task(n)
        elif ch=="4":
            break
        else:
            print("wrong choice!!")

main()