# Simple in-memory storage for tasks.
# In production, replace this with persistent storage (e.g., a database).

from .models import Task


class TaskStorage:
    """In-memory storage for Task objects."""
    _tasks = {}

    @classmethod
    # PUBLIC_INTERFACE
    def add_task(cls, title):
        """Adds a new task and returns the Task object."""
        task = Task(title=title)
        cls._tasks[task.id] = task
        return task

    @classmethod
    # PUBLIC_INTERFACE
    def get_task(cls, task_id):
        """Retrieves a Task by its ID."""
        return cls._tasks.get(task_id)

    @classmethod
    # PUBLIC_INTERFACE
    def update_task(cls, task_id, title=None, completed=None):
        """Updates an existing Task and returns it."""
        task = cls.get_task(task_id)
        if not task:
            return None
        if title is not None:
            task.title = title
        if completed is not None:
            task.completed = completed
        task.updated_at = Task().updated_at  # update timestamp
        return task

    @classmethod
    # PUBLIC_INTERFACE
    def delete_task(cls, task_id):
        """Deletes a Task by id."""
        return cls._tasks.pop(task_id, None)

    @classmethod
    # PUBLIC_INTERFACE
    def list_tasks(cls):
        """Returns a list of all tasks."""
        return list(cls._tasks.values())

    @classmethod
    # PUBLIC_INTERFACE
    def mark_task_completed(cls, task_id, completed=True):
        """Marks a task as completed."""
        task = cls.get_task(task_id)
        if not task:
            return None
        task.completed = completed
        task.updated_at = Task().updated_at
        return task
