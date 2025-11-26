from flask import Blueprint, request, jsonify

validate_identity_bp = Blueprint('validate_identity', __name__)

@validate_identity_bp.route('/validate_identity', methods=['POST'])
def validate_identity():
    """
    Endpoint para validar la identidad de un usuario.
    """
    try:
        data = request.json

        # Validar que el campo 'identity_data' esté presente
        if not data or 'identity_data' not in data:
            return jsonify({
                "status": "error",
                "message": "The 'identity_data' field is required."
            }), 400

        identity_data = data['identity_data']

        # Validar que los campos requeridos estén presentes
        if 'TipoDocumento' not in identity_data or 'NumeroIdentificacion' not in identity_data:
            return jsonify({
                "status": "error",
                "message": "Both 'TipoDocumento' and 'NumeroIdentificacion' are required."
            }), 400

        tipo_documento = identity_data['TipoDocumento']
        numero_identificacion = str(identity_data['NumeroIdentificacion'])

        # Validar los valores
        if tipo_documento not in ['CC', 'TI', 'CE', 'PT']:
            return jsonify({
                "status": "error",
                "message": f"Invalid 'TipoDocumento': {tipo_documento}. Must be one of ['CC', 'TI', 'CE', 'PT']."
            }), 400

        if len(numero_identificacion) < 5:
            return jsonify({
                "status": "error",
                "message": "Identity must have at least 5 characters."
            }), 400

        # Simulación de éxito
        return jsonify({
            "status": "success",
            "message": "Identity validated successfully."
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"An error occurred: {str(e)}"
        }), 500

# The JavaScript code has been moved to a separate file (validate_identity.js).
# Ensure to include the script in your HTML file.