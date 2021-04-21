from flask import Flask, Blueprint, jsonify, make_response
from flask_restplus import Api
from flask_cors import CORS
from flask_mail import Mail
import os
import sys
import socket
from datetime import datetime
from utils.helpers import calculate_proc_time


# Initialize application
app = Flask(__name__)
# Enabling cors
CORS(app)
app_settings = os.getenv(
    'APP_SETTINGS', 'app.config.DevelopmentConfig'
)
mail = Mail(app)

# app configuration
app.config.from_object(app_settings)


blueprint = Blueprint('api', __name__)
api = Api(blueprint, version='1.0', title='API',
          description='description of swagger')

# each module should be import here
# import app.Login.views as login_view



# register namespace for swagger UI
# api.add_namespace(login_view.login_ns)
# api.add_namespace(login_view.forgot_password_ns)



# api.namespaces.clear()
# app.register_blueprint(blueprint)


@app.route('/about')
@app.route('/')
@calculate_proc_time
def test():
    func_resp = {}
    pc_name = socket.gethostname()
    func_resp['message'] = "backend server working fine."
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
