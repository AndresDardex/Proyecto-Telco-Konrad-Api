from flask import Blueprint, request, jsonify

documentos_bp = Blueprint('documents', __name__)

# Datos quemados para documentos
DOCUMENTS = []

@documentos_bp.route('/documents', methods=['POST'])
def manage_documents():
    data = request.json
    if not data or 'document_data' not in data:
        return jsonify({"error": "The 'document_data' field is required"}), 400

    document_data = data['document_data']
    if 'document_type' not in document_data or 'content' not in document_data:
        return jsonify({"error": "The 'document_data' must contain 'document_type' and 'content'"}), 400

    DOCUMENTS.append(document_data)
    return jsonify({"status": "success", "message": "Document managed successfully", "document_data": document_data})