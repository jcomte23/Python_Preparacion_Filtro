import moduls.messages as msgs


def create_task(tasks, new_task):
    tasks.append(new_task)
    print(msgs.task_entered)
    print("-" * msgs.characters)


def delete_task(tasks, query):
    coincidence = False
    for task in tasks:
        if query in task:
            index = tasks.index(task)
            print(f"[{index}]: '{task}'")
            coincidence = True
    if coincidence:
        try:
            deleted_task = int(input('Enter the ID number of the task you want to delete->'))
            if 0 <= deleted_task < len(tasks):
                print(f"    '{tasks[deleted_task]}' will be removed, are you sure?")
                confirm = int(input(f"    [1]YES [0]NO =>"))
                if confirm == 1:
                    del tasks[deleted_task]
                    print(msgs.task_deleted)
                    print("-" * msgs.characters)
                elif confirm == 0:
                    print("-" * msgs.characters)
                else:
                    print(msgs.invalid_option)
                    print("-" * msgs.characters)
            else:
                print(msgs.no_results_found)
                print("-" * msgs.characters)
        except ValueError:
            print(msgs.invalid_option)
            print("-" * msgs.characters)

    elif not coincidence:
        print(msgs.no_results_found)


def list_task(tasks):
    if not tasks:
        print(msgs.no_results_found)
        print("-" * msgs.characters)
    else:
        print("_" * msgs.characters)
        print(msgs.pending_task)
        tasks.sort()
        for task in tasks:
            print(f"* {task}")
        print("-" * msgs.characters)


def show_menu():
    print("-" * msgs.characters)
    print("|  [1] List tasks   |  [2] New task  |  [3] Update task |  [4] Delete task  |  [5] Exit   |")
    print("-" * msgs.characters)


def update_task(tasks, query):
    coincidence = False
    for task in tasks:
        if query in task:
            index = tasks.index(task)
            print(f"[{index}]: '{task}'")
            coincidence = True
    if coincidence:
        try:
            index = int(input('Enter the ID number of the task you want to update ->'))
            if 0 <= index < len(tasks):
                tasks[index] = input("  Enter the new text for this task= ")
                print(msgs.task_updated)
                print("-" * msgs.characters)
            else:
                print(msgs.no_results_found)
                print("-" * msgs.characters)
        except ValueError:
            print(msgs.invalid_option)
            print("-" * msgs.characters)
    elif not coincidence:
        print(msgs.no_results_found)
