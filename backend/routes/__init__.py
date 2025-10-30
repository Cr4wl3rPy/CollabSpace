# Este archivo hace que routes/ sea un paquete Python
# Puede estar vacío o importar los blueprints

from routes.auth import auth_bp
from routes.rooms import rooms_bp

__all__ = ['auth_bp', 'rooms_bp']