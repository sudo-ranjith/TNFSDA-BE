from flask import request, jsonify
from flask_restplus import Resource, Namespace, fields
import jwt
from werkzeug.security import check_password_hash

# module imports
from app import app, mongo, bcrypt
import app.Login.serializers as login_serializers
# import app.Login.models as login_models
import app.Login.helpers as login_helpers
import app.Common.helpers as common_helpers
import app.Common.serializers as common_serializers

# login namespace
login_ns = Namespace('Login', description='Login operations')
logout_ns = Namespace('Logout', description='Logout operations')
forgot_password_ns = Namespace('Forgotpassword', description='Forgot Password')
app_config = app.config


# login
@login_ns.route('')
class Login(Resource):
    """
    Login Class which contains methods to login
    """

    # POST
    @login_ns.expect(login_serializers.login_api_model, validate=True)
    @login_ns.response(200, app.config["SUCCESS_MESSAGE_200"], login_serializers.login_success_model)
    @login_ns.response(301, app.config["FAILURE_MESSAGE_301"], common_serializers.response_api_model)
    @login_ns.response(400, app.config["FAILURE_MESSAGE_400"], common_serializers.response_api_model)
    @login_ns.response(401, app.config["FAILURE_MESSAGE_401"], common_serializers.response_api_model)
    @login_ns.response(403, app.config["FAILURE_MESSAGE_403"], common_serializers.response_api_model)
    @login_ns.response(404, app.config["FAILURE_MESSAGE_404"], common_serializers.response_api_model)
    @login_ns.response(409, app.config["FAILURE_MESSAGE_409"], common_serializers.response_api_model)
    @login_ns.response(422, app.config["FAILURE_MESSAGE_422"], common_serializers.response_api_model)
    @login_ns.response(500, app.config["FAILURE_MESSAGE_500"], common_serializers.response_api_model)
    def post(self):
        """
        POST method to login
        """
        try:
            # invalid request format
            if not (request.content_type == 'application/json'):
                return common_helpers.response('failed',
                                               app.config["FAILURE_MESSAGE_400"],
                                               'Content type should be application/json',
                                               [], 400)
            # token payload
            post_data = request.get_json()
            username = post_data.get('username')
            password = post_data.get('password')
            email = post_data.get('email')
            
            register_col = mongo.db.get('REGISTRATION_COL')
            registered_username = register_col.find_one({'username': username})      
            if not registered_username:
                pw_hash = bcrypt.generate_password_hash(password)
                #pw_hash=str(pw_hash)
                register_db.insert_one({'username': username , 'password': pw_hash , 'mobile': mobile})
                result_msg = {'msg': 'registered succesfully'}
            # user_exists = login_models.LoginCurb().read_data(check_patient_exists_query)
            if user_exists["exists"] is False:
                more_info = "user not exists"
                return common_helpers.response('failed',
                                               app.config["FAILURE_MESSAGE_404"],
                                               more_info, [], 404)
            patient_id = "'" + user_exists["item"][0] + "'"
            check_user_exists_query = "select password from USERS where patient_id = {}".format(patient_id)
            # user_exists = login_models.LoginCurb().read_data(check_user_exists_query)
            if user_exists["exists"] is False:
                more_info = "user not exists"
                return common_helpers.response('failed',
                                               app.config["FAILURE_MESSAGE_404"],
                                               more_info, [], 404)
            if password != user_exists["item"][0]:
                more_info = "Password Incorrect"
                return common_helpers.response('failed',
                                               app.config["FAILURE_MESSAGE_401"],
                                               more_info, [], 401)
            patient_id = patient_id.replace("'", "")
            encode_token = login_helpers.encode_auth_token(patient_id, civic_id)
            credentials = {
                "patient_id": patient_id,
                "auth_token": encode_token,
            }
            return login_helpers.response('success',
                                          app.config["SUCCESS_MESSAGE_200"],
                                          'Successfully Logged in',
                                          credentials,
                                          200)

            # response failed
        except Exception as e:
            more_info = "Unable to login a user : Exception occurred -" + str(e)
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)


@forgot_password_ns.route('')
class ForgotPassword(Resource):
    """
    ForgotPassword Class which contains methods to sent password  to registered mail
    """

    # POST
    @forgot_password_ns.expect(login_serializers.forget_password, validate=True)
    @forgot_password_ns.response(200, app.config["SUCCESS_MESSAGE_200"], login_serializers.login_success_model)
    @forgot_password_ns.response(301, app.config["FAILURE_MESSAGE_301"], common_serializers.response_api_model)
    @forgot_password_ns.response(400, app.config["FAILURE_MESSAGE_400"], common_serializers.response_api_model)
    @forgot_password_ns.response(401, app.config["FAILURE_MESSAGE_401"], common_serializers.response_api_model)
    @forgot_password_ns.response(403, app.config["FAILURE_MESSAGE_403"], common_serializers.response_api_model)
    @forgot_password_ns.response(404, app.config["FAILURE_MESSAGE_404"], common_serializers.response_api_model)
    @forgot_password_ns.response(409, app.config["FAILURE_MESSAGE_409"], common_serializers.response_api_model)
    @forgot_password_ns.response(422, app.config["FAILURE_MESSAGE_422"], common_serializers.response_api_model)
    @forgot_password_ns.response(500, app.config["FAILURE_MESSAGE_500"], common_serializers.response_api_model)
    def post(self):
        """
        POST method to Forgot password
        """
        try:
            # invalid request format
            if not (request.content_type == 'application/json'):
                return common_helpers.response('failed',
                                               app.config["FAILURE_MESSAGE_400"],
                                               'Content type should be application/json',
                                               [], 400)
            # token payload
            post_data = request.get_json()
            civic_id = "'" + post_data.get('email_civic_id') + "'"
            check_patient_exists_query = "select patient_id,email from PATIENT where " \
                                         "civic_id = {} or email = {} and is_registered = 1".format(civic_id, civic_id)
            # patient_exists = login_models.LoginCurb().read_data(check_patient_exists_query)
            if patient_exists["exists"] is False:
                more_info = "Enter Email ID or Civic Id not registered"
                return common_helpers.response('failed',
                                               app.config["FAILURE_MESSAGE_404"],
                                               more_info, [], 404)
            patient_id = "'" + patient_exists["item"][0] + "'"
            check_user_exists_query = "select password from USERS where patient_id = {}".format(patient_id)
            # user_exists = login_models.LoginCurb().read_data(check_user_exists_query)
            if user_exists["exists"] is False:
                more_info = "user not exists"
                return common_helpers.response('failed',
                                               app.config["FAILURE_MESSAGE_404"],
                                               more_info, [], 404)
            password = user_exists["item"][0]
            email = patient_exists["item"][1]
            common_helpers.sent_mail(email, password)
            return common_helpers.response_json('success',
                                                app.config["SUCCESS_MESSAGE_200"],
                                                'Password has sent to Registered Mail',
                                                [],
                                                200)

        except Exception as e:
            more_info = "Unable to perform forgot password operation : Exception occurred -" + str(e)
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)
