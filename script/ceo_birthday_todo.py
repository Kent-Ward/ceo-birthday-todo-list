# --- CEO's Birthday Party To-Do List Manager ---

todo_list = {
    "Drinks": ["Angry Orchids", "Sparkling Water", "Stella Artois Cidre"],
    "Foods": ["Daug Haus Catering", "Peacock Indian Catering", "GAF Dessert Catering"],
    "Games": ["Trivia Challenge", "Dance Battle", "Karaoke Contest"],
    "Music": ["Lofi Trap Beats", "2009 Party Mix", "Live DJ Booking"],
    "Location": ["RoofTop Garden", "Backup: Meeting Room 10th Floor"],
    "Gifts": ["Gift Card to Spa", "5Day Virgin Voyage Cruise"]
}

completed_tasks = []

def display_list():
    print("\n--- TO-DO LIST ---")
    for category, tasks in todo_list.items():
        print(f"\n{category}:")
        for task in tasks:
            status = "✅" if task in completed_tasks else "❌"
            print(f"  [{status}] {task}")
    print()

def mark_task_complete():
    display_list()
    task_to_complete = input("Enter the exact task you completed: ").strip()
    if any(task_to_complete in tasks for tasks in todo_list.values()):
        if task_to_complete not in completed_tasks:
            completed_tasks.append(task_to_complete)
            print(f"Marked '{task_to_complete}' as completed!\n")
        else:
            print("Task is already marked as completed.\n")
    else:
        print("Task not found in the list.\n")

def add_new_task():
    category = input("Enter the category: ").strip()
    task = input("Enter the task: ").strip()
    if category in todo_list:
        todo_list[category].append(task)
    else:
        todo_list[category] = [task]
    print(f"Added '{task}' under '{category}'.\n")

def view_completed_tasks():
    print("\n--- COMPLETED TASKS ---")
    if completed_tasks:
        for task in completed_tasks:
            print(f"  ✅ {task}")
    else:
        print("  No tasks completed yet.")
    print()

def delete_task():
    display_list()  
    task_to_delete = input("Enter the exact task you want to delete: ").strip()
    for category, tasks in todo_list.items():
        if task_to_delete in tasks:
            tasks.remove(task_to_delete)
            if task_to_delete in completed_tasks:
                completed_tasks.remove(task_to_delete)
            print(f"Deleted '{task_to_delete}' from '{category}'.\n")
            return
    print("Task not found in the list.\n")


def main():
    print("Welcome to the CEO's Birthday Party To-Do List Manager!")
    
    while True:
        print("\nMenu Options:")
        print("1. View To-Do List")
        print("2. Mark Task as Completed")
        print("3. Add New Task")
        print("4. Delete a Task")
        print("5. View Completed Tasks")
        print("6. Exit\n")

        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            display_list()
        elif choice == "2":
            mark_task_complete()
        elif choice == "3":
            add_new_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            view_completed_tasks()
        elif choice == "6":
            print("Goodbye! Happy Planning!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()