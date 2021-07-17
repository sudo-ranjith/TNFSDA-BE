from flask import request
from flask_restplus import Resource, Namespace
import app.login.model as login_model
import app.login.serializers as login_serializers
from app import app, bcrypt
import app.Common.serializers as common_serializers
import app.Common.helpers as common_helpers
from datetime import  datetime
import traceback
from flask_jwt_simple import JWTManager, jwt_required, create_jwt, get_jwt_identity


login_ns = Namespace('login', description='user login')


@login_ns.route('')
class Login(Resource):
    """
         This class get form data
         @return: success or failure message
    """

    @login_ns.expect(login_serializers.login, validate=True)
    @login_ns.response(200, app.config["SUCCESS_MESSAGE_200"], login_serializers.login)
    @login_ns.response(301, app.config["FAILURE_MESSAGE_301"], common_serializers.response_api_model)
    @login_ns.response(400, app.config["FAILURE_MESSAGE_400"], common_serializers.response_api_model)
    @login_ns.response(401, app.config["FAILURE_MESSAGE_401"], common_serializers.response_api_model)
    @login_ns.response(403, app.config["FAILURE_MESSAGE_403"], common_serializers.response_api_model)
    @login_ns.response(404, app.config["FAILURE_MESSAGE_404"], common_serializers.response_api_model)
    @login_ns.response(409, app.config["FAILURE_MESSAGE_409"], common_serializers.response_api_model)
    @login_ns.response(422, app.config["FAILURE_MESSAGE_422"], common_serializers.response_api_model)
    @login_ns.response(500, app.config["FAILURE_MESSAGE_500"], common_serializers.response_api_model)
    def post(self):
        try:
            if not (request.content_type == 'application/json'):
                return common_helpers.response('failed',
                                               app.config["FAILURE_MESSAGE_400"],
                                               'Content type should be application/json',
                                               [], 400)
            post_data = request.get_json()
            password = post_data.get("password")
            rank = post_data.get("rank")
            id_number = post_data.get("id_number")

            check_existing_query = {"id_number":  id_number, "rank": rank}

            registeration_obj = login_model.RegisterCurb()
            user_data = registeration_obj.read_data(check_existing_query)
            if not user_data["exists"]:
                more_info = "User does not exists {}".format(user_data)
                return common_helpers.response('failed', app.config["FAILURE_MESSAGE_422"],
                                            more_info,
                                            [], 422)
            existing_encrypted_password = user_data['data'].get("password")
            decrypted_password = bcrypt.check_password_hash(existing_encrypted_password,password)

            if not decrypted_password:
                more_info = "Please enter valid password"
                return common_helpers.response('failed', app.config["FAILURE_MESSAGE_422"],
                                            more_info,
                                            [], 422)


            post_data['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
            post_data['active'] = 1
            # post_data['token'] = create_jwt(email)
            del post_data['password']
            # user_item = login_model.RegisterCurb()
            # user_item = user_item.find_modify({'email': email}, post_data)

            more_info = "Successfully Logged in"
            return common_helpers.response('success',
                                           app.config["SUCCESS_MESSAGE_200"],
                                           more_info,
                                           [post_data['rank']],
                                           200,
                                           post_data['id_number'])
        except Exception as e:
            e = f"{traceback.format_exc()}"
            more_info = "Unable to Inserted data :Exception occurred - " + str(e)
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)