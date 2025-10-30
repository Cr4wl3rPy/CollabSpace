from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import random
import string

# db se inicializa en app.py, aquí solo lo importamos
db = SQLAlchemy()


class User(db.Model):
    """Modelo de Usuario"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    avatar_color = db.Column(db.String(7), default='#667eea')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    # Relaciones
    rooms_created = db.relationship('Room', backref='creator', lazy=True, foreign_keys='Room.created_by')
    messages = db.relationship('Message', backref='author', lazy=True)
    
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if not self.avatar_color:
            self.avatar_color = self._generate_random_color()
    
    def set_password(self, password):
        """Hashear la contraseña"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verificar contraseña"""
        return check_password_hash(self.password_hash, password)
    
    @staticmethod
    def _generate_random_color():
        """Generar color hex aleatorio para el avatar"""
        colors = [
            '#667eea', '#764ba2', '#f093fb', '#4facfe',
            '#43e97b', '#fa709a', '#fee140', '#30cfd0'
        ]
        return random.choice(colors)
    
    def to_dict(self):
        """Convertir usuario a diccionario (sin password)"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'avatar_color': self.avatar_color,
            'created_at': self.created_at.isoformat()
        }
    
    def __repr__(self):
        return f'<User {self.username}>'


class Room(db.Model):
    """Modelo de Sala de Colaboración"""
    __tablename__ = 'rooms'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(6), unique=True, nullable=False, index=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    max_users = db.Column(db.Integer, default=50)
    
    # Relaciones
    messages = db.relationship('Message', backref='room', lazy=True, cascade='all, delete-orphan')
    
    def __init__(self, **kwargs):
        super(Room, self).__init__(**kwargs)
        if not self.code:
            self.code = self._generate_room_code()
    
    @staticmethod
    def _generate_room_code():
        """Generar código único de 6 dígitos para la sala"""
        while True:
            code = ''.join(random.choices(string.digits, k=6))
            # Verificar que no exista
            if not Room.query.filter_by(code=code).first():
                return code
    
    def to_dict(self):
        """Convertir sala a diccionario"""
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat(),
            'is_active': self.is_active,
            'max_users': self.max_users
        }
    
    def __repr__(self):
        return f'<Room {self.name} ({self.code})>'


class Message(db.Model):
    """Modelo de Mensaje de Chat"""
    __tablename__ = 'messages'
    
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    def to_dict(self):
        """Convertir mensaje a diccionario"""
        return {
            'id': self.id,
            'room_id': self.room_id,
            'user_id': self.user_id,
            'username': self.author.username,
            'avatar_color': self.author.avatar_color,
            'content': self.content,
            'sent_at': self.sent_at.isoformat()
        }
    
    def __repr__(self):
        return f'<Message {self.id} in Room {self.room_id}>'