# from termcolor import colored

# list = []

# def start_todo():

#   while True:
#     request = input(colored("""Choose action:
#     Type any task you want to add
#     View: to view your list
#     Complete: to mark task as complete
#     Remove: to remove task
#     Quit: to quit program
#   >  """,'cyan'))
#     if request.lower() == 'quit':
#       print(f'Your to-do list: {list}')
#       print('Program ended')
#       quit()
#     elif request.lower() == 'view':
#       print(list)
#     elif request.lower() == 'complete':
#       print(list)
#       modify_task = input('Placement # of task to complete: ')
#       list[int(modify_task)][1] = 'complete'
#       print(list)
#     elif request.lower() == 'remove':
#       print(list)
#       remove_task = input('Placement # of task to remove: ')
#       list.pop(int(remove_task))
#       print(list)
#     else:
#       add_task = request
#       task_status = 'incomplete'
#       list.append([add_task,task_status])
#       print(list)


# start_todo()


# ChatGPT response below:
# It was really cool to see how the logic was similar but here are the biggest things I learned
# You can make very small things a function! (like a menu function, an add task function, a view
# menu function that gets referenced in the remove task function)
# I also learned a new function -- enumerate. I'll practice this next!


def display_menu():
    print("\nTo-Do List Manager")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({'task': task, 'completed': False})
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return

    for i, task in enumerate(tasks, 1):
        status = "Completed" if task['completed'] else "Not completed"
        print(f"{i}. {task['task']} - {status}")

def mark_task_completed(tasks):
    if not tasks:
        print("No tasks to mark as completed.")
        return

    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]['completed'] = True
        print(f"Task '{tasks[task_num - 1]['task']}' marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks(tasks)
    task_num = int(input("Enter the task number to remove: "))
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task['task']}' removed.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Exiting the to-do list manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":  main()