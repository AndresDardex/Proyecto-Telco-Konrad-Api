from flask import Blueprint, jsonify

# Crear el blueprint para solicitudes
solicitudes_bp = Blueprint('requests', __name__)

# Datos quemados para solicitudes
REQUESTS = {
    "1234": {"status": "pending", "details": "Request is being processed"},
    "5678": {"status": "completed", "details": "Request completed successfully"}
}

@solicitudes_bp.route('/<request_id>', methods=['GET'])
def request_status(request_id):
    """
    Endpoint para obtener el estado de una solicitud por su ID.
    """
    if request_id in REQUESTS:
        return jsonify({
            "status": "success",
            "request": REQUESTS[request_id]
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": "Request ID not found"
        }), 404

# Manejo de errores globales para rutas no encontradas
@solicitudes_bp.app_errorhandler(404)
def not_found_error(error):
    return jsonify({
        "status": "error",
        "message": "The requested resource was not found"
    }), 404

# Manejo de errores globales para errores internos del servidor
@solicitudes_bp.app_errorhandler(500)
def internal_error(error):
    return jsonify({
        "status": "error",
        "message": "An internal server error occurred"
    }), 500