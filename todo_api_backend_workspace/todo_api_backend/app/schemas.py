# Marshmallow schemas for API serialization/deserialization

from marshmallow import Schema, fields


# PUBLIC_INTERFACE
class TaskSchema(Schema):
    """Schema for serializing Task objects."""
    id = fields.String(dump_only=True, description="Unique identifier for the task")
    title = fields.String(required=True, description="Title of the task")
    completed = fields.Boolean(missing=False, description="Task completion status")
    created_at = fields.DateTime(dump_only=True, description="Timestamp when task was created")
    updated_at = fields.DateTime(dump_only=True, description="Timestamp of last task update")


# PUBLIC_INTERFACE
class TaskCreateSchema(Schema):
    """Schema for task creation input."""
    title = fields.String(required=True, description="Title of the task")


# PUBLIC_INTERFACE
class TaskUpdateSchema(Schema):
    """Schema for updating an existing task."""
    title = fields.String(required=False, description="Title of the task")
    completed = fields.Boolean(required=False, description="Task completion status")
