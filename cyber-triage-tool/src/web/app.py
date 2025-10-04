from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def index():
        return {"status": "ok", "message": "Cyber Triage Tool Web UI (stub)"}

    return app

