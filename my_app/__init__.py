import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv()


db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
login_manager = LoginManager()

login_manager.login_view = 'auth_bp.auth'  
login_manager.login_message = 'Пожалуйста, войдите в систему, чтобы получить доступ к этой странице.'
login_manager.login_message_category = 'info'


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    instance_path = app.instance_path


    db_path = os.path.join(instance_path, 'my_app.db')

    default_db_uri = f"sqlite:///{db_path}"

    db_uri = os.getenv('DATABASE_URL') or default_db_uri

    if db_uri.startswith("postgres://"):
        db_uri = db_uri.replace("postgres://", "postgresql://", 1)

    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=db_uri
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    login_manager.init_app(app)

    from .main_bp import main_bp
    from .register_bp import register_bp
    from .auth_bp import auth_bp
    from .add_bp import add_bp
    from .api_bp import api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(register_bp, url_prefix='/register')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(add_bp, url_prefix='/add')
    app.register_blueprint(api_bp, url_prefix='/api')

    return app