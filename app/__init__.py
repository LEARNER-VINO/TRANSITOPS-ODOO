from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///transitops.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app)
    db.init_app(app)

    from app.routes.dashboard import dashboard_bp

    app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")

    with app.app_context():
        from app import seed

        db.create_all()
        seed.seed_database()

    return app
