# Simple in-memory model for Task management.
# In production, replace this with a database model.

from uuid import uuid4
from datetime import datetime


class Task:
    """Task represents a to-do item."""
    def __init__(self, title, completed=False):
        self.id = str(uuid4())
        self.title = title
        self.completed = completed
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
