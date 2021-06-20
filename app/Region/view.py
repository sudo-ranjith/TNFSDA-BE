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


region = Namespace('region', description='region details')


@region.route('')
class Login(Resource):
    """
         This class get form data
         @return: success or failure message
     """

    @region.expect(login_serializers.login, validate=True)
    @region.response(200, app.config["SUCCESS_MESSAGE_200"], login_serializers.login)
    @region.response(301, app.config["FAILURE_MESSAGE_301"], common_serializers.response_api_model)
    @region.response(400, app.config["FAILURE_MESSAGE_400"], common_serializers.response_api_model)
    @region.response(401, app.config["FAILURE_MESSAGE_401"], common_serializers.response_api_model)
    @region.response(403, app.config["FAILURE_MESSAGE_403"], common_serializers.response_api_model)
    @region.response(404, app.config["FAILURE_MESSAGE_404"], common_serializers.response_api_model)
    @region.response(409, app.config["FAILURE_MESSAGE_409"], common_serializers.response_api_model)
    @region.response(422, app.config["FAILURE_MESSAGE_422"], common_serializers.response_api_model)
    @region.response(500, app.config["FAILURE_MESSAGE_500"], common_serializers.response_api_model)
    def post(self):
        try:
            if not (request.content_type == 'application/json'):
                return common_helpers.response('failed',
                                               app.config["FAILURE_MESSAGE_400"],
                                               'Content type should be application/json',
                                               [], 400)
            post_data = request.get_json()
            email = post_data.get("email")
            password = post_data.get("password")
            rank = post_data.get("rank")
        
        except Exception as e:
            e = f"{traceback.format_exc()}"
            more_info = "Unable to Inserted data :Exception occurred - " + str(e)
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)