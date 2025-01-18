from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
        print("Tables created")

    from .routes import api_bp
    app.register_blueprint(api_bp)

    return app
