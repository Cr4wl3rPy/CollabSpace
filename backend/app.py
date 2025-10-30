from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config

# Inicializar extensiones
db = SQLAlchemy()
socketio = SocketIO()
jwt = JWTManager()

def create_app(config_class=Config):
    """Factory pattern para crear la aplicación Flask"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Inicializar extensiones con la app
    db.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*")
    jwt.init_app(app)
    CORS(app)
    
    # Crear tablas de base de datos
    with app.app_context():
        db.create_all()
        print("✅ Database tables created successfully")
    
    # Registrar Blueprints (rutas) después de crear tablas
    from routes.auth import auth_bp
    from routes.rooms import rooms_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(rooms_bp, url_prefix='/api/rooms')
    
    # Registrar event handlers de SocketIO
    from sockets import chat, whiteboard, presence
    
    # Rutas básicas
    @app.route('/')
    def index():
        return jsonify({
            'message': 'CollabSpace API',
            'version': '1.0.0',
            'status': 'running',
            'database': 'SQLite'
        })
    
    @app.route('/health')
    def health():
        return jsonify({'status': 'healthy'})
    
    return app

# Crear instancia de la app
app = create_app()

if __name__ == '__main__':
    # Correr con SocketIO
    print("🚀 Starting CollabSpace Backend...")
    print("📊 Database: SQLite (collabspace.db)")
    print("🌐 Server: http://localhost:5000")
    
    socketio.run(
        app,
        debug=True,
        host='0.0.0.0',
        port=5000,
        allow_unsafe_werkzeug=True
    )