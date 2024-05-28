#!/usr/bin/python3
"""Contains a Flask web application API.
"""
import os
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
"""The Flask web application instance."""
app.config['JSONIFY_BOLDPRINT_REGULAR'] = True
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app, resources={'/*': {'origins': app_host}})

app.config['SWAGGER'] = {
    "swagger_version": "2.0",
    "title": "Flasgger",
    "headers": [
        ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS),
        ('Access-Control-Allow-Origin', '*"),
        ('Access-Control-Allow-Credentials', "true"),
    ],
    "specs": [
        {
            "title": "HBNB API",
            "description": "AirBnB RESTful API",
            "version": "1",
            "endpoint": 'v1_views',
            "route": '/v1/views',
        }
    ]
}
Swagger(app)


@app.teardown_appcontext
def teardown_flask(code):
    '''The Flask app/request context end event listener.'''
    storage.close()


@app.errorhandler(404)
def error_404(error):
    '''Handles the 404 HTTP error code.'''
    return jsonify(error='Not found'), 404


@app.errorhandler(400)
def error_400(error):
    '''Handles the 400 HTTP error code.'''
    msg = 'Bad request'
    if isinstance(error, Exception) and hasattr(error, 'description'):
        msg = error.description
    return jsonify(error=msg), 400


if __name__ == '__main__':
    app_host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    app_port = os.environ.get('HBNB_API_PORT', '5000')
    app.run(host=app_host, port=app_port, threaded=True)
