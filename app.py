from flask import Flask
from app.api import init_app  # Importar la función para inicializar la API

app = Flask(__name__)

# Inicializar la API con el blueprint principal
init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)