import moduls.messages as msgs
import moduls.operations as ops

print()
print("-" * msgs.characters)
print("|                                       TO-DO LIST                                        |")

tasks = []

while True:
    ops.show_menu()
    try:
        option = int(input("->"))
        if option == 1:
            ops.list_task(tasks)
        elif option == 2:
            new_task = input("Enter the new task=> ").lower().strip()
            ops.create_task(tasks, new_task)
        elif option == 3:
            query = input("Search task for keyword => ").lower().strip()
            ops.update_task(tasks, query)
        elif option == 4:
            query = input("Search task for keyword  => ").lower().strip()
            ops.delete_task(tasks, query)
        elif option == 5:
            exit()
        else:
            print(msgs.invalid_option)
            print("-" * msgs.characters)
    except ValueError:
        print(msgs.invalid_option)
        print("-" * msgs.characters)
