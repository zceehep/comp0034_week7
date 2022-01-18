from flask import Flask


def create_app(config_class_name):
    """
    Initialise the Flask application.
    :type config_class_name: Specifies the configuration class
    :rtype: Returns a configured Flask object
    """
    app = Flask(__name__)

    from my_flask_app.main.routes import main_bp
    app.register_blueprint(main_bp)

    from my_flask_app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    return app
