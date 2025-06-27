import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///my_app.db',
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    from .main_bp import main_bp
    from .register_bp import register_bp
    from .auth_bp import auth_bp
    from .add_bp import add_bp

    app.register_blueprint(main_bp, url_prefix='/home')
    app.register_blueprint(register_bp, url_prefix='/register')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(add_bp, url_prefix='/add')

    return app