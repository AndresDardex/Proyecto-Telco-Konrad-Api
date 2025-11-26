from flask import Blueprint, request, jsonify

contratos_bp = Blueprint('contracts', __name__)

# Datos quemados para contratos
CONTRACTS = []

@contratos_bp.route('/contracts', methods=['POST'])
def digital_contracts():
    data = request.json
    if not data or 'contract_data' not in data:
        return jsonify({"error": "The 'contract_data' field is required"}), 400

    contract_data = data['contract_data']
    if 'contract_id' not in contract_data or 'details' not in contract_data:
        return jsonify({"error": "The 'contract_data' must contain 'contract_id' and 'details'"}), 400

    CONTRACTS.append(contract_data)
    return jsonify({"status": "success", "message": "Contract processed successfully", "contract_data": contract_data})