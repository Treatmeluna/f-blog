from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    
    return app