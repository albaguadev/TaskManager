import json

class Task:

    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{status}] #{self.id}: {self.description}"

class TaskManager:

    FILENAME = "tasks.json"

    def __init__(self):
        self._tasks = []
        self._next_id = 1
        self.load_tasks(self.FILENAME)

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Task added: {description}")
        self.save_tasks(self.FILENAME)

    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Task deleted: {task.description}")
                self.save_tasks(self.FILENAME)
                return
        print(f"Task with ID {id} not found.")

    def complete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.mark_completed()
                print (f"Task completed: {task.description}")
                self.save_tasks(self.FILENAME)
                return
        print(f"Task with ID {id} not found.")

    def list_tasks(self):
        if not self._tasks:
            print("No tasks available.")
            return
        for task in self._tasks:
            print(task)
    
    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            json.dump([task.__dict__ for task in self._tasks], file, indent=4)

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self._tasks = [Task(item["id"], item["description"], item["completed"]) for item in data]
                self._next_id = max([task.id for task in self._tasks], default=0) + 1
        except FileNotFoundError:
            self._tasks = []