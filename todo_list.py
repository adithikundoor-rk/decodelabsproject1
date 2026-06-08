import json
import os

# --- MODEL (Data Logic) ---
# This dictionary will serve as our "In-Memory Database" 
# structure: { task_id (int): { "task": str, "status": str } }
todo_database = {}
DATA_FILE = "todo_data.json"

def load_data():
    """Loads tasks from a permanent JSON disk file (Persistence)."""
    global todo_database
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                # Convert string keys back to integers for consistent indexing
                data = json.load(file)
                todo_database = {int(k): v for k, v in data.items()}
        except Exception:
            todo_database = {}
    else:
        todo_database = {}

def save_data():
    """Serializes data to disk so it survives a process termination."""
    with open(DATA_FILE, "w") as file:
        json.dump(todo_database, file, indent=4)

def add_task(task_name):
    """Generates a unique ID and appends a new task."""
    next_id = max(todo_database.keys(), default=0) + 1
    todo_database[next_id] = {
        "task": task_name,
        "status": "Pending"
    }
    save_data()

def get_all_tasks():
    """Returns the current database snapshot."""
    return todo_database

def delete_task(task_id):
    """Removes a task by its specific key identifier."""
    if task_id in todo_database:
        del todo_database[task_id]
        save_data()
        return True
    return False


# --- VIEW & CONTROLLER (User Interface Logic) ---
def display_menu():
    """Prints a clean industrial CLI interface."""
    print("\n" + "="*40)
    print("      DECODELABS BACKEND TASK ENGINE     ")
    print("="*40)
    print("[1] View Active Tasks")
    print("[2] Append New Task")
    print("[3] Delete Terminated Task")
    print("[4] Exit Engine")
    print("="*40)

def view_tasks_ui():
    tasks = get_all_tasks()
    if not tasks:
        print("\n[!] The in-memory database is empty.")
        return

    print("\n--- CURRENT TASK REGISTRY ---")
    # Using pythonic enumeration tracking for visual cleanliness
    for index, (task_id, details) in enumerate(tasks.items(), start=1):
        print(f"{index}. [ID: {task_id}] {details['task']} | Status: {details['status']}")

def add_task_ui():
    task_name = input("\nEnter task specifications: ").strip()
    if task_name:
        add_task(task_name)
        print("[✓] Task committed to volatile storage and synchronized to disk.")
    else:
        print("[X] Task description cannot be blank.")

def delete_task_ui():
    view_tasks_ui()
    tasks = get_all_tasks()
    if not tasks:
        return
        
    try:
        target_id = int(input("\nEnter the specific [ID] to delete: "))
        if delete_task(target_id):
            print(f"[✓] Task ID {target_id} safely purged from records.")
        else:
            print("[X] Error: Provided ID does not exist in registry.")
    except ValueError:
        print("[X] Invalid Input: Please enter a valid numerical integer ID.")

def main():
    """Core runtime engine execution loop."""
    load_data()  # Pull data from disk on startup
    
    while True:
        display_menu()
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            view_tasks_ui()
        elif choice == '2':
            add_task_ui()
        elif choice == '3':
            delete_task_ui()
        elif choice == '4':
            print("\nShutting down engine gracefully. Goodbye developer!")
            break
        else:
            print("[X] Invalid instruction sequence. Choose options 1 through 4.")


# --- THE GATEKEEPER ---
# Ensures the module runs natively when executed directly 
if __name__ == "__main__":
    main()