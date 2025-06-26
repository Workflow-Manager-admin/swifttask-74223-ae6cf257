from flask_smorest import Blueprint
from flask.views import MethodView
from ..schemas import TaskSchema, TaskCreateSchema, TaskUpdateSchema
from ..storage import TaskStorage

blp = Blueprint(
    "tasks",
    "tasks",
    url_prefix="/api/tasks",
    description="Endpoints for managing to-do tasks."
)


# PUBLIC_INTERFACE
@blp.route("/")
class TaskListResource(MethodView):
    """Handles retrieving all tasks and creating tasks."""

    @blp.response(200, TaskSchema(many=True), description="List all tasks")
    def get(self):
        """Get all tasks."""
        return [task.to_dict() for task in TaskStorage.list_tasks()]

    @blp.arguments(TaskCreateSchema, location="json")
    @blp.response(201, TaskSchema, description="Task successfully created")
    def post(self, new_data):
        """Create a new task."""
        task = TaskStorage.add_task(title=new_data["title"])
        return task.to_dict()


# PUBLIC_INTERFACE
@blp.route("/<string:task_id>")
class TaskResource(MethodView):
    """Handles retrieving, updating, and deleting an individual task."""

    @blp.response(200, TaskSchema, description="Get a task by ID")
    def get(self, task_id):
        """Get task by ID."""
        task = TaskStorage.get_task(task_id)
        if not task:
            blp.abort(404, message="Task not found.")
        return task.to_dict()

    @blp.arguments(TaskUpdateSchema, location="json")
    @blp.response(200, TaskSchema, description="Task successfully updated")
    def put(self, update_data, task_id):
        """Update a task."""
        task = TaskStorage.update_task(
            task_id,
            title=update_data.get("title"),
            completed=update_data.get("completed"),
        )
        if not task:
            blp.abort(404, message="Task not found.")
        return task.to_dict()

    @blp.response(204, description="Task successfully deleted")
    def delete(self, task_id):
        """Delete a task."""
        deleted = TaskStorage.delete_task(task_id)
        if not deleted:
            blp.abort(404, message="Task not found.")
        return "", 204


# PUBLIC_INTERFACE
@blp.route("/<string:task_id>/complete")
class TaskCompleteResource(MethodView):
    """Endpoint for marking a task as completed or not completed."""

    @blp.arguments(TaskUpdateSchema, location="json")
    @blp.response(200, TaskSchema, description="Task marked as completed/uncompleted")
    def patch(self, update_data, task_id):
        """Mark a task as completed or not completed."""
        completed = update_data.get("completed", True)
        task = TaskStorage.mark_task_completed(task_id, completed=completed)
        if not task:
            blp.abort(404, message="Task not found.")
        return task.to_dict()
