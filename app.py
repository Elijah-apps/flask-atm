from flask import Flask
from atm.routes import initialize_routes
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Swagger configuration
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "ATM API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

initialize_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
