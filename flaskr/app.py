from flask import Flask
from flask_cors import CORS

from config import config

# Routes
from routes import User
from routes import Owner
from routes import PieceOfLand
from routes import DetailPieceOfLand

app = Flask(__name__)

CORS(app, resources={"*": {"origins": "http://localhost:5000"}})


def page_not_found(error):
    return "<h1>Not found page</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(User.usuario, url_prefix='/api/usuario')
    app.register_blueprint(Owner.propietario, url_prefix='/api/propietario')
    app.register_blueprint(PieceOfLand.predio, url_prefix='/api/predio')
    app.register_blueprint(DetailPieceOfLand.detallePredio, url_prefix='/api/detallePredio')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()