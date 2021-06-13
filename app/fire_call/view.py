from flask import request
from flask_restplus import Resource, Namespace
import app.fire_call.model as fire_call_model
import app.fire_call.serializers as fire_call_serializers
from app import app, bcrypt
import app.Common.serializers as common_serializers
import app.Common.helpers as common_helpers
from datetime import  datetime
import traceback
from flask_jwt_simple import JWTManager, jwt_required, get_jwt_identity
from bson import json_util


fire_cal = Namespace('fire_call', description='fire call api')


@fire_cal.route('')
# @jwt_required
class Login(Resource):
    """
         This class get form data
         @return: success or failure message
     """

    @fire_cal.expect(fire_call_serializers.fire_call, validate=True)
    @fire_cal.response(200, app.config["SUCCESS_MESSAGE_200"], fire_call_serializers.fire_call)
    @fire_cal.response(301, app.config["FAILURE_MESSAGE_301"], common_serializers.response_api_model)
    @fire_cal.response(400, app.config["FAILURE_MESSAGE_400"], common_serializers.response_api_model)
    @fire_cal.response(401, app.config["FAILURE_MESSAGE_401"], common_serializers.response_api_model)
    @fire_cal.response(403, app.config["FAILURE_MESSAGE_403"], common_serializers.response_api_model)
    @fire_cal.response(404, app.config["FAILURE_MESSAGE_404"], common_serializers.response_api_model)
    @fire_cal.response(409, app.config["FAILURE_MESSAGE_409"], common_serializers.response_api_model)
    @fire_cal.response(422, app.config["FAILURE_MESSAGE_422"], common_serializers.response_api_model)
    @fire_cal.response(500, app.config["FAILURE_MESSAGE_500"], common_serializers.response_api_model)
    def post(self):
        try:
            if not (request.content_type == 'application/json'):
                return common_helpers.response('failed',
                                               app.config["FAILURE_MESSAGE_400"],
                                               'Content type should be application/json',
                                               [], 400)
            post_data = request.get_json()
            token = post_data.get("token")
            current_user = get_jwt_identity()
            # check user has valid access token

            post_data['created_at'] = datetime.now().strftime('%Y%m%d%H%M%S%f')
            post_data['created_by'] = current_user
            post_data['active'] = 1
            user_item = fire_call_model.RegisterCurb()
            user_item = user_item.insert_data(post_data)

            more_info = "Successfully inserted firecall data"
            return common_helpers.response('success',
                                           app.config["SUCCESS_MESSAGE_200"],
                                           more_info,
                                           [],
                                           200,
                                           post_data.get('token'))
        except Exception as e:
            e = f"{traceback.format_exc()}"
            more_info = "Unable to Inserted data :Exception occurred - " + str(e)
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)

@fire_cal.route('/count')
# @jwt_required
class Login(Resource):
    """
         This class get form data
         @return: success or failure message
     """

    @fire_cal.response(200, app.config["SUCCESS_MESSAGE_200"], fire_call_serializers.fire_call)
    @fire_cal.response(301, app.config["FAILURE_MESSAGE_301"], common_serializers.response_api_model)
    @fire_cal.response(400, app.config["FAILURE_MESSAGE_400"], common_serializers.response_api_model)
    @fire_cal.response(401, app.config["FAILURE_MESSAGE_401"], common_serializers.response_api_model)
    @fire_cal.response(403, app.config["FAILURE_MESSAGE_403"], common_serializers.response_api_model)
    @fire_cal.response(404, app.config["FAILURE_MESSAGE_404"], common_serializers.response_api_model)
    @fire_cal.response(409, app.config["FAILURE_MESSAGE_409"], common_serializers.response_api_model)
    @fire_cal.response(422, app.config["FAILURE_MESSAGE_422"], common_serializers.response_api_model)
    @fire_cal.response(500, app.config["FAILURE_MESSAGE_500"], common_serializers.response_api_model)
    def get(self):
        try:
            # post_data['created_by'] = current_user
            user_item = fire_call_model.RegisterCurb()
            user_item = user_item.get_count()
            # user_item = json_util.dumps(user_item)

            more_info = "Successfully fetched firecall count"
            return common_helpers.response('success',
                                           app.config["SUCCESS_MESSAGE_200"],
                                           more_info,
                                           user_item,
                                           200)
        except Exception as e:
            e = f"{traceback.format_exc()}"
            more_info = "Unable to Inserted data :Exception occurred - " + str(e)
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)
