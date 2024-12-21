def add_task(tasks,title,description,priority="low"):
    task=(title,description,priority)
    tasks.append(task)
    print(f"task'{title}' added successfully!")
def remove_task(tasks,title):
    tasks=[task for task in tasks if task.title!=title]
    print(f"task '{title}' removed successfully!")
    return tasks
def mark_completed(tasks,title):
    for task in tasks:
        if task.title==title:
            task.mark_complete()
            print(f"task '{title}'marked as completed!")
def list_tasks(tasks):
    if not tasks:
        print("No tasks to display")
        return
    for task in tasks:
        print(task)
def save_tasks_to_file(tasks,filename="tasks.json"):
    with open(filename,"w") as file:
        json.dump([task.__dict__ for task in tasks], file)
def load_tasks_from_file(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            task_data = json.load(file)
            tasks = [task(**data) for data in task_data]
        return tasks
    except FileNotFoundError:
        return []


