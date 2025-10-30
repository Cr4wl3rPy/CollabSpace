from flask_socketio import emit
from app import socketio


@socketio.on('draw')
def handle_draw(data):
    """
    Manejar evento de dibujo en el whiteboard
    
    data = {
        'room_id': int,
        'user_id': int,
        'path': {canvas path data from Fabric.js},
        'tool': str,  # 'pen', 'eraser', 'shape', etc.
        'color': str,
        'width': int
    }
    """
    try:
        room_id = data.get('room_id')
        
        if not room_id:
            emit('error', {'message': 'Room ID is required'})
            return
        
        # Broadcast a todos en la sala EXCEPTO al que dibujó
        emit('canvas_update', data, room=f'room_{room_id}', include_self=False)
        
    except Exception as e:
        emit('error', {'message': str(e)})


@socketio.on('clear_canvas')
def handle_clear_canvas(data):
    """
    Limpiar el canvas completamente
    
    data = {
        'room_id': int,
        'user_id': int
    }
    """
    try:
        room_id = data.get('room_id')
        user_id = data.get('user_id')
        
        if not room_id:
            emit('error', {'message': 'Room ID is required'})
            return
        
        # Broadcast a todos en la sala
        emit('canvas_cleared', {
            'room_id': room_id,
            'cleared_by': user_id
        }, room=f'room_{room_id}')
        
    except Exception as e:
        emit('error', {'message': str(e)})


@socketio.on('cursor_move')
def handle_cursor_move(data):
    """
    Manejar movimiento del cursor de un usuario
    
    data = {
        'room_id': int,
        'user_id': int,
        'username': str,
        'x': float,
        'y': float,
        'color': str
    }
    """
    try:
        room_id = data.get('room_id')
        
        if not room_id:
            return
        
        # Broadcast posición del cursor a todos EXCEPTO al que lo movió
        emit('cursor_update', data, room=f'room_{room_id}', include_self=False)
        
    except Exception as e:
        emit('error', {'message': str(e)})


@socketio.on('undo')
def handle_undo(data):
    """
    Deshacer última acción en el canvas
    
    data = {
        'room_id': int,
        'user_id': int
    }
    """
    try:
        room_id = data.get('room_id')
        
        if not room_id:
            emit('error', {'message': 'Room ID is required'})
            return
        
        # Broadcast a todos en la sala
        emit('canvas_undo', data, room=f'room_{room_id}')
        
    except Exception as e:
        emit('error', {'message': str(e)})