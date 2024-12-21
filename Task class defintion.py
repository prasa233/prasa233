import json
class Task:
    def __init__(self,title,description,priority="low"):
        self.title=title
        self.description= description
        self.completed =False
        self.priority=priority
    def mark_complete(self):
        self.completed =True
    def __str__(self):
        status="Done"if self.completed else "pending"
        return f"{self.title}-{self.priority} priority -{status}"