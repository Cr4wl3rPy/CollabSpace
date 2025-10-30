from flask_socketio import emit
from app import socketio
from models import db, Message, User, Room


@socketio.on('send_message')
def handle_send_message(data):
    """Manejar envío de mensaje de chat"""
    try:
        room_id = data.get('room_id')
        user_id = data.get('user_id')
        content = data.get('content', '').strip()
        
        if not room_id or not user_id or not content:
            emit('error', {'message': 'Missing required fields'})
            return
        
        room = Room.query.get(room_id)
        if not room:
            emit('error', {'message': 'Room not found'})
            return
        
        user = User.query.get(user_id)
        if not user:
            emit('error', {'message': 'User not found'})
            return
        
        message = Message(
            room_id=room_id,
            user_id=user_id,
            content=content
        )
        db.session.add(message)
        db.session.commit()
        
        emit('new_message', message.to_dict(), room=f'room_{room_id}')
        
    except Exception as e:
        db.session.rollback()
        emit('error', {'message': str(e)})


@socketio.on('typing')
def handle_typing(data):
    """Manejar indicador de usuario está escribiendo"""
    try:
        room_id = data.get('room_id')
        user_id = data.get('user_id')
        username = data.get('username')
        is_typing = data.get('is_typing', False)
        
        emit('user_typing', {
            'user_id': user_id,
            'username': username,
            'is_typing': is_typing
        }, room=f'room_{room_id}', include_self=False)
        
    except Exception as e:
        emit('error', {'message': str(e)})