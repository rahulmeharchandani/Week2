class ToDoList:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_task()
        
    def load_task(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    task, status = line.strip().split("|", 1)
                    self.tasks.append({"task": task, "completed": status.lower() == "true"})
        except FileNotFoundError:
            pass
        
    def save_task(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task['task']}|{task['completed']}\n")
                
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_task()
        print("Task added successfully.")
        
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for index, task in enumerate(self.tasks, start=1):
            status = "[Done]" if task["completed"] else "[ ]"
            print(f"{index}. {status} {task['task']}")
            
    def mark_complete(self, task_num):
        if 1 <= task_num <= len(self.tasks):
            self.tasks[task_num - 1]["completed"] = True
            self.save_task()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
            
    def delete_task(self, task_num):
        if 1 <= task_num <= len(self.tasks):
            self.tasks.pop(task_num - 1)
            self.save_task()
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
            

def main():
    todo = ToDoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter a choice: ")
        if choice == "1":
            task = input("Enter a task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.view_tasks()
            try:
                task_num = int(input("Enter task number to mark as completed: "))
                todo.mark_complete(task_num)
            except ValueError:
                print("Enter a valid number.")
        elif choice == "4":
            todo.view_tasks()
            try:
                task_num = int(input("Enter task number to delete: "))
                todo.delete_task(task_num)
            except ValueError:
                print("Enter a valid number.")
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")
                
if __name__ == "__main__":
    main()
