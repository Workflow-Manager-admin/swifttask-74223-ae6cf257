from app import app

if __name__ == "__main__":
    # PUBLIC_INTERFACE
    # Runs the Flask application on port 5001 instead of the default 5000.
    app.run(port=5001)
