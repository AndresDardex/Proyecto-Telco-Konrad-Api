class Config:
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'sqlite:///telco_konrad.db'
    SECRET_KEY = 'supersecretkey'
    JWT_SECRET_KEY = 'your_jwt_secret_key_here'
    API_VERSION = 'v1'
    PORT = 5000
    BASE_API_URL = '/api'  # Definir la URL base para los endpoints