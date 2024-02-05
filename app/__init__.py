from flask import Flask
from .webhook_listener import webhook_listener


def create_app():
    app = Flask(__name__)

    # Register the webhook listener blueprint
    app.register_blueprint(webhook_listener)

    return app
