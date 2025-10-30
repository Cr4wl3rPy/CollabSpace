from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Room, Message

rooms_bp = Blueprint('rooms', __name__)


@rooms_bp.route('/', methods=['GET'])
@jwt_required()
def get_rooms():
    """Obtener todas las salas activas"""
    try:
        rooms = Room.query.filter_by(is_active=True).order_by(Room.created_at.desc()).all()
        return jsonify({'rooms': [room.to_dict() for room in rooms]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@rooms_bp.route('/', methods=['POST'])
@jwt_required()
def create_room():
    """Crear nueva sala"""
    try:
        current_user_id = get_jwt_identity()
        data = request.get_json()
        
        if not data or not data.get('name'):
            return jsonify({'error': 'Room name is required'}), 400
        
        name = data.get('name').strip()
        
        if len(name) < 3:
            return jsonify({'error': 'Room name must be at least 3 characters'}), 400
        
        room = Room(name=name, created_by=current_user_id)
        
        db.session.add(room)
        db.session.commit()
        
        return jsonify({
            'message': 'Room created successfully',
            'room': room.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@rooms_bp.route('/join', methods=['POST'])
@jwt_required()
def join_room():
    """Unirse a una sala mediante código"""
    try:
        data = request.get_json()
        
        if not data or not data.get('code'):
            return jsonify({'error': 'Room code is required'}), 400
        
        code = data.get('code').strip()
        room = Room.query.filter_by(code=code, is_active=True).first()
        
        if not room:
            return jsonify({'error': 'Room not found or inactive'}), 404
        
        return jsonify({
            'message': 'Room found',
            'room': room.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@rooms_bp.route('/<int:room_id>', methods=['GET'])
@jwt_required()
def get_room(room_id):
    """Obtener información de una sala específica"""
    try:
        room = Room.query.get(room_id)
        
        if not room:
            return jsonify({'error': 'Room not found'}), 404
        
        return jsonify({'room': room.to_dict()}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@rooms_bp.route('/<int:room_id>/messages', methods=['GET'])
@jwt_required()
def get_room_messages(room_id):
    """Obtener mensajes de una sala"""
    try:
        room = Room.query.get(room_id)
        
        if not room:
            return jsonify({'error': 'Room not found'}), 404
        
        limit = request.args.get('limit', 50, type=int)
        
        messages = Message.query.filter_by(room_id=room_id)\
            .order_by(Message.sent_at.desc())\
            .limit(limit)\
            .all()
        
        messages.reverse()
        
        return jsonify({
            'messages': [msg.to_dict() for msg in messages]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500