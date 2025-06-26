# Registers all blueprints for different API endpoints.

from .tasks import blp as tasks_blp
from .health import blp as health_blp

blueprints = [tasks_blp, health_blp]