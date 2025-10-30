from flask import request
from flask_socketio import emit, join_room, leave_room, disconnect
from app import socketio
from models import User, Room

# Diccionario en memoria para trackear usuarios conectados
# Formato: { 'room_123': { 'user_456': { 'username': 'Juan', 'sid': 'abc123' } } }
connected_users = {}


@socketio.on('connect')
def handle_connect():
    """Cliente se conecta al servidor WebSocket"""
    print(f'Client connected: {request.sid}')
    emit('connected', {'message': 'Connected to CollabSpace server'})


@socketio.on('disconnect')
def handle_disconnect():
    """Cliente se desconecta"""
    print(f'Client disconnected: {request.sid}')
    
    # Remover usuario de todas las salas donde estaba
    for room_key in list(connected_users.keys()):
        for user_id in list(connected_users[room_key].keys()):
            if connected_users[room_key][user_id].get('sid') == request.sid:
                username = connected_users[room_key][user_id].get('username')
                
                # Remover del diccionario
                del connected_users[room_key][user_id]
                
                # Si la sala queda vacía, eliminarla
                if not connected_users[room_key]:
                    del connected_users[room_key]
                
                # Notificar a otros usuarios
                emit('user_left', {
                    'user_id': user_id,
                    'username': username,
                    'users_online': len(connected_users.get(room_key, {}))
                }, room=room_key)


@socketio.on('join_room')
def handle_join_room(data):
    """
    Usuario se une a una sala
    
    data = {
        'room_id': int,
        'user_id': int
    }
    """
    try:
        room_id = data.get('room_id')
        user_id = data.get('user_id')
        
        if not room_id or not user_id:
            emit('error', {'message': 'Missing room_id or user_id'})
            return
        
        # Verificar que la sala existe
        room = Room.query.get(room_id)
        if not room or not room.is_active:
            emit('error', {'message': 'Room not found or inactive'})
            return
        
        # Verificar que el usuario existe
        user = User.query.get(user_id)
        if not user:
            emit('error', {'message': 'User not found'})
            return
        
        room_key = f'room_{room_id}'
        
        # Unir al cliente a la sala de SocketIO
        join_room(room_key)
        
        # Agregar a diccionario de usuarios conectados
        if room_key not in connected_users:
            connected_users[room_key] = {}
        
        connected_users[room_key][user_id] = {
            'username': user.username,
            'avatar_color': user.avatar_color,
            'sid': request.sid
        }
        
        # Obtener lista de usuarios online
        users_online = [
            {
                'user_id': int(uid),
                'username': info['username'],
                'avatar_color': info['avatar_color']
            }
            for uid, info in connected_users[room_key].items()
        ]
        
        # Notificar al usuario que se unió exitosamente
        emit('joined_room', {
            'room': room.to_dict(),
            'users_online': users_online
        })
        
        # Notificar a otros usuarios que alguien se unió
        emit('user_joined', {
            'user_id': user_id,
            'username': user.username,
            'avatar_color': user.avatar_color,
            'users_online': len(users_online)
        }, room=room_key, include_self=False)
        
        print(f'User {user.username} joined room {room.name}')
        
    except Exception as e:
        emit('error', {'message': str(e)})
        print(f'Error in join_room: {str(e)}')


@socketio.on('leave_room')
def handle_leave_room(data):
    """
    Usuario sale de una sala
    
    data = {
        'room_id': int,
        'user_id': int
    }
    """
    try:
        room_id = data.get('room_id')
        user_id = data.get('user_id')
        
        if not room_id or not user_id:
            return
        
        room_key = f'room_{room_id}'
        
        # Salir de la sala de SocketIO
        leave_room(room_key)
        
        # Remover del diccionario
        if room_key in connected_users and user_id in connected_users[room_key]:
            username = connected_users[room_key][user_id].get('username')
            del connected_users[room_key][user_id]
            
            # Si la sala queda vacía, eliminarla
            if not connected_users[room_key]:
                del connected_users[room_key]
            
            # Notificar a otros usuarios
            emit('user_left', {
                'user_id': user_id,
                'username': username,
                'users_online': len(connected_users.get(room_key, {}))
            }, room=room_key)
            
            print(f'User {username} left room {room_id}')
        
    except Exception as e:
        print(f'Error in leave_room: {str(e)}')


@socketio.on('get_online_users')
def handle_get_online_users(data):
    """
    Obtener lista de usuarios conectados en una sala
    
    data = {
        'room_id': int
    }
    """
    try:
        room_id = data.get('room_id')
        
        if not room_id:
            emit('error', {'message': 'Room ID is required'})
            return
        
        room_key = f'room_{room_id}'
        
        users_online = [
            {
                'user_id': int(uid),
                'username': info['username'],
                'avatar_color': info['avatar_color']
            }
            for uid, info in connected_users.get(room_key, {}).items()
        ]
        
        emit('online_users', {
            'room_id': room_id,
            'users': users_online,
            'count': len(users_online)
        })
        
    except Exception as e:
        emit('error', {'message': str(e)})