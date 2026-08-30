from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app_factory import db
from models import User

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    """Get all users (admin only)"""
    user_id = get_jwt_identity()
    current_user = User.query.get(user_id)
    
    if not current_user or current_user.role != 'admin':
        return jsonify({'message': 'Unauthorized'}), 403
    
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 50, type=int)
    role = request.args.get('role')
    status = request.args.get('status')
    
    query = User.query
    
    if role:
        query = query.filter_by(role=role)
    if status:
        query = query.filter_by(status=status)
    
    users = query.paginate(page=page, per_page=limit)
    
    return jsonify({
        'users': [u.to_dict() for u in users.items],
        'page': page,
        'limit': limit,
        'total': users.total
    }), 200

@admin_bp.route('/users/<int:user_id>/suspend', methods=['POST'])
@jwt_required()
def suspend_user(user_id):
    """Suspend a user"""
    admin_id = get_jwt_identity()
    admin = User.query.get(admin_id)
    
    if not admin or admin.role != 'admin':
        return jsonify({'message': 'Unauthorized'}), 403
    
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    data = request.get_json()
    reason = data.get('reason', 'No reason provided')
    
    user.status = 'suspended'
    db.session.commit()
    
    return jsonify({
        'message': 'User suspended successfully',
        'user': user.to_dict()
    }), 200

@admin_bp.route('/analytics', methods=['GET'])
@jwt_required()
def get_analytics():
    """Get platform analytics"""
    user_id = get_jwt_identity()
    current_user = User.query.get(user_id)
    
    if not current_user or current_user.role != 'admin':
        return jsonify({'message': 'Unauthorized'}), 403
    
    # TODO: Calculate analytics
    return jsonify({
        'total_users': 0,
        'active_users': 0,
        'total_trades': 0,
        'trading_volume': 0,
        'average_return': 0
    }), 200

@admin_bp.route('/settings', methods=['GET'])
@jwt_required()
def get_settings():
    """Get platform settings"""
    user_id = get_jwt_identity()
    current_user = User.query.get(user_id)
    
    if not current_user or current_user.role != 'admin':
        return jsonify({'message': 'Unauthorized'}), 403
    
    # TODO: Get settings from database
    return jsonify({
        'initial_balance': 10000,
        'commission_rate': 0.001,
        'market_open_hour': 9,
        'market_close_hour': 16
    }), 200

@admin_bp.route('/settings', methods=['PUT'])
@jwt_required()
def update_settings():
    """Update platform settings"""
    user_id = get_jwt_identity()
    current_user = User.query.get(user_id)
    
    if not current_user or current_user.role != 'admin':
        return jsonify({'message': 'Unauthorized'}), 403
    
    data = request.get_json()
    
    # TODO: Update settings in database
    return jsonify({
        'message': 'Settings updated successfully',
        'settings': data
    }), 200
