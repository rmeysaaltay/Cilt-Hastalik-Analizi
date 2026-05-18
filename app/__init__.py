from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'app/static/uploads'
    app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
    app.config['SECRET_KEY'] = 'gizli-anahtar'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cilt.db'

    db.init_app(app)

    from .routes.upload import upload_bp
    from .routes.analysis import analysis_bp
    from .routes.history import history_bp
    from .routes.main import main_bp

    app.register_blueprint(upload_bp)
    app.register_blueprint(analysis_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app