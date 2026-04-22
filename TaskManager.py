# Final Exam AIDI 2004 - Andrew Sharland

class TaskManager:
    def addTask(self, title, priority):
        print(f"Task added: {title} with priority {priority}")

    def deleteTask(self, task_id):
        """Deletes a task by its ID"""
        print(f"Task {task_id} deleted")