def add_tasks(tasks):
    while True:
        task = input("Enter the task: (Press Enter to finish)")  
        if task.strip() == "":
            break
        tasks.append(task)
def show_tasks(tasks):
            if not tasks:
                print("No tasks yet")
            else:
                print("\n-------------- Your tasks ----------------\n")
                for i, item in enumerate(tasks, start=1):
                    print(f"{i}. {item}")
                print("\n ----------------Ends of Tasks ------------------")
def edit_tasks(tasks):
    if not tasks:
          print("No tasks yet")
    else:
        show_tasks(tasks)
        try:
            task_num = int(input("Enter choice to edit task: "))
        except ValueError:
            print("Please Enter a Number")
            return 
        if 1<=task_num <= len(tasks):
           edited_task = input("enter the new text: ")
           tasks[task_num-1] = edited_task
        else:
            print("invalid task number")

def delete_tasks(tasks):
    if not tasks:
        print("No tasks yet")
    else:
        show_tasks(tasks)
        try:
            task_num = int(input("Enter choice to delete task: "))
        except ValueError:
            print("Please enter a number")
            return
        if 1<=task_num <= len(tasks):
            tasks.pop(task_num-1)
            print("Task deleted")
        else:
            print("invalid task number")
def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
   
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return[line.strip() for line in f.readlines()]
    except FileNotFoundError:
         return []
tasks = load_tasks()
while True:
    print("1. Add Task \n2. Show Tasks \n3. Edit Tasks \n4. Delete Tasks \n5. Quit")
    choice = input("Choose Task:")
    if choice==  "1":
        add_tasks(tasks)
        save_tasks(tasks)
    elif choice == "2":
        show_tasks(tasks)
    elif choice == '3':
        edit_tasks(tasks)
        save_tasks(tasks)
    elif choice== "4":
        delete_tasks(tasks)
        save_tasks(tasks)
    elif choice=="5":
        break
    else:
        print("Invalid Choice")
