from flask import Blueprint

# Crear el blueprint principal para la API
api_bp = Blueprint('api', __name__)

# Importar los endpoints desde solicitudes.py y otros módulos
from .solicitudes import solicitudes_bp

# Registrar los blueprints específicos en el blueprint principal
api_bp.register_blueprint(solicitudes_bp, url_prefix='/requests')

def init_app(app):
    """
    Inicializar la aplicación Flask con el blueprint principal.
    """
    app.register_blueprint(api_bp, url_prefix='/api')