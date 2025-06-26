from flask import Flask
from flask_cors import CORS
from flask_smorest import Api

from .routes import blueprints

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config["API_TITLE"] = "To-Do List API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config['OPENAPI_URL_PREFIX'] = '/docs'
app.config["OPENAPI_SWAGGER_UI_PATH"] = ""
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
# Register all blueprints defined in routes/__init__.py
for blp in blueprints:
    api.register_blueprint(blp)
