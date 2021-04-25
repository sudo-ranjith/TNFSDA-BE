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

# Initialize application
app = Flask(__name__)
# Enabling cors
CORS(app)
app_settings = os.getenv(
    'APP_SETTINGS', 'app.config.DevelopmentConfig'
)
mail = Mail(app)

# each module should be import here
app.config['MONGO_DBNAME'] = 'btkguzctt6o97cb'
app.config['MONGO_URI'] = f'mongodb://ufumtyzgd9ji6x7g50f8:VJxXRkNWzzZq1EeokkGK@btkguzctt6o97cb-mongodb.services.clever-cloud.com:27017/btkguzctt6o97cb'
app.config['SECRET_KEY'] = 'a5ea0c77491f965420dfa379ddb6105adb0e3e88'
app.config['JWT_SECRET_KEY'] = 'super-secret' 

mongo = PyMongo(app)
bcrypt = Bcrypt(app)

# app configuration
app.config.from_object(app_settings)


blueprint = Blueprint('api', __name__)
api = Api(blueprint, version='1.0', title='API',
          description='description of swagger')

import app.Login.views as login_view
import app.Register.view as register_view


# register namespace for swagger UI
api.add_namespace(login_view.login_ns)
api.add_namespace(login_view.forgot_password_ns)
api.add_namespace(register_view.register)



api.namespaces.clear()
app.register_blueprint(blueprint)
api.add_namespace(register_view.register)


@app.route('/about')
@app.route('/')
@calculate_proc_time
def test():
    func_resp = {}
    pc_name = socket.gethostname()
    func_resp['message'] = "Application API working fine."
    func_resp['status'] = "success"
    func_resp['server_name'] = pc_name
    func_resp['os'] = sys.platform
    func_resp['now_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return func_resp


@app.errorhandler(404)
def not_found(error):
    func_resp = {}
    func_resp['now_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    func_resp['message'] = "Please check the End Point, API End Point is not available"
    func_resp['status'] = "failed"
    return make_response(jsonify(func_resp), 404)
