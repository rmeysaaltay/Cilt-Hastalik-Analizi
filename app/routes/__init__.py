from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'app/static/uploads'
    app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
    app.config['SECRET_KEY'] = 'gizli-anahtar'

    from .routes.upload import upload_bp
    app.register_blueprint(upload_bp)

    return app