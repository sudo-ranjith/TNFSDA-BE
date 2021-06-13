from flask import Flask, Blueprint, jsonify, make_response
from flask_restplus import Api
from flask_cors import CORS
from flask_mail import Mail
import os
import sys
import socket
from datetime import datetime
from utils.helpers import calculate_proc_time
from flask_pymongo import PyMongo
from app.config import BaseConfig
from flask_bcrypt import Bcrypt
from flask_jwt_simple import JWTManager
from werkzeug.contrib.fixers import ProxyFix


# Initialize application
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
# Enabling cores
CORS(app)
if os.environ.get('FLASK_ENV'):
    env = os.environ.get('FLASK_ENV')
    if env == "development":
        app_settings = os.getenv('APP_SETTINGS', 'app.config.DevelopmentConfig')
    elif env == "qa":
        app_settings = os.getenv('APP_SETTINGS', 'app.config.TestingConfig')
    elif env == "prod":
        app_settings = os.getenv('APP_SETTINGS', 'app.config.ProductionConfig')
    else:
        print("Given ENV is not configured")
else:
    app_settings = os.getenv('APP_SETTINGS', 'app.config.DevelopmentConfig')
# app configuration
app.config.from_object(app_settings)
mail = Mail(app)

# each module should be import here

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

blueprint = Blueprint('api', __name__)
api = Api(blueprint, version='1.0', title='API', prefix = '/api',
          description='description of swagger')

import app.login.view as login_view
import app.Register.view as register_view
import app.fire_call.view as fire_call_view
import app.rescue_call.view as rescue_call_view


# register namespace for swagger UI
api.add_namespace(register_view.register)
api.add_namespace(login_view.login_ns)
api.add_namespace(fire_call_view.fire_cal)
api.add_namespace(rescue_call_view.resuce)

api.namespaces.clear()
app.register_blueprint(blueprint)

api.add_namespace(register_view.register)
api.add_namespace(login_view.login_ns)
api.add_namespace(fire_call_view.fire_cal)
api.add_namespace(rescue_call_view.resuce)


@app.route('/about')
@calculate_proc_time
def test():
    func_resp = dict()
    pc_name = socket.gethostname()
    func_resp['message'] = "Application API working fine."
    func_resp['status'] = "success"
    func_resp['server_name'] = pc_name
    func_resp['os'] = sys.platform
    func_resp['now_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return func_resp


@app.errorhandler(404)
def not_found(error):
    func_resp = {'now_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 'message': "Please check the End Point, API End Point is not available", 'status': "failed"}
    return make_response(jsonify(func_resp), 404)
