tasks = []


def add_task(task):
    tasks.append(task)
    print(f"Task'{task}' Added")


def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Removed '{task}'")
    else:
        print("Task not found.")


def show_all_task():
    print("Your ToDu-list")
    for show in tasks:
        print(f"{show}")


while True:
    action = int(
        input(
            """
        1. Add Task
        2. Remove Task
        3. Show Task
        4. Exit
    Enter the Value : """
        )
    )
    if action == 1:
        task = input("Enter A Task : ")
        add_task(task)
    elif action == 2:
        task = input("Enter task to remove : ")
        remove_task(task)
    elif action == 3:
        show_all_task()
    elif action == 4:
        break
    else:
        print("Invalid action, try again.")
