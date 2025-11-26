from flask import Flask, render_template
from app.api.endpoints import api_bp
from app.api.enrolamiento import enrolamiento_bp
from app.api.documentos import documentos_bp
from app.api.contratos import contratos_bp
from app.api.solicitudes import solicitudes_bp

class Config:
    BASE_API_URL = '/api'

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # Cargar la configuración desde config.py
    app.config["SECRET_KEY"] = "supersecretkey"

    # Registrar los blueprints para los endpoints API
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(enrolamiento_bp, url_prefix='/api/enrollment')
    app.register_blueprint(documentos_bp, url_prefix='/api')
    app.register_blueprint(contratos_bp, url_prefix='/api')
    app.register_blueprint(solicitudes_bp, url_prefix='/api/requests')

    # Rutas para servir las páginas HTML (sin prefijo /api/)
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/validate_identity')
    def validate_identity_page():
        return render_template('validate_identity.html')

    @app.route('/enrollment')
    def enrollment_page():
        return render_template('enrollment.html')

    @app.route('/document_management')
    def document_management_page():
        return render_template('documents.html')

    @app.route('/digital_contracts')
    def digital_contracts_page():
        return render_template('contracts.html')

    @app.route('/request_status')
    def request_status_page():
        return render_template('request_status.html')

    @app.context_processor
    def inject_base_url():
        return {'BASE_API_URL': app.config['BASE_API_URL']}  # Inyectar BASE_API_URL en los templates

    return app