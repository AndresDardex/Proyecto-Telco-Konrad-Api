from flask import Blueprint, request, jsonify
from app.services.service_logic import ServiceLogic  # Importar la clase ServiceLogic

api_bp = Blueprint('api', __name__)
service_logic = ServiceLogic()  # Crear una instancia de ServiceLogic

# Validar Identidad
@api_bp.route('/validate_identity', methods=['POST'])
def validate_identity():
    data = request.json
    if not data or 'identity_data' not in data:
        return jsonify({"error": "The 'identity_data' field is required"}), 400

    identity_data = data['identity_data']
    result = service_logic.validate_identity(identity_data)
    return jsonify(result)

# Enrolamiento
@api_bp.route('/enrollment', methods=['POST'])
def enrollment():
    data = request.json
    if not data or 'user_data' not in data:
        return jsonify({"error": "The 'user_data' field is required"}), 400

    user_data = data['user_data']
    result = service_logic.enroll_user(user_data)
    return jsonify(result)

# Gestión de Documentos
@api_bp.route('/documents', methods=['POST'])
def document_management():
    data = request.json
    if not data or 'document_data' not in data:
        return jsonify({"error": "El campo 'document_data' es obligatorio"}), 400

    document_data = data['document_data']
    if not isinstance(document_data, dict) or 'document_type' not in document_data or 'content' not in document_data:
        return jsonify({"error": "El campo 'document_data' debe contener 'document_type' y 'content'"}), 400

    result = service_logic.manage_documents(document_data)
    return jsonify(result)

# Contratos Digitales
@api_bp.route('/contracts', methods=['POST'])
def digital_contracts():
    data = request.json
    if not data or 'contract_data' not in data:
        return jsonify({"error": "El campo 'contract_data' es obligatorio"}), 400

    contract_data = data['contract_data']
    if not isinstance(contract_data, dict) or 'contract_id' not in contract_data or 'details' not in contract_data:
        return jsonify({"error": "El campo 'contract_data' debe contener 'contract_id' y 'details'"}), 400

    result = service_logic.digital_contracts(contract_data)
    return jsonify(result)

# Estado de Solicitudes
@api_bp.route('/request_status/<request_id>', methods=['GET'])
def request_status(request_id):
    if not request_id.isdigit():
        return jsonify({"error": "El 'request_id' debe ser un número válido"}), 400

    result = service_logic.request_status(request_id)
    return jsonify(result)