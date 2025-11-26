from flask import Blueprint, request, jsonify

enrolamiento_bp = Blueprint('enrollment', __name__)

# Datos quemados para enrolamiento
ENROLLED_USERS = []

@enrolamiento_bp.route('/enrollment', methods=['POST'])
def enroll_user():
    data = request.json
    if not data or 'user_data' not in data:
        return jsonify({"error": "The 'user_data' field is required"}), 400

    user_data = data['user_data']
    if 'name' not in user_data or 'email' not in user_data:
        return jsonify({"error": "The 'user_data' must contain 'name' and 'email'"}), 400

    ENROLLED_USERS.append(user_data)
    return jsonify({"status": "success", "message": "User enrolled successfully", "user_data": user_data})