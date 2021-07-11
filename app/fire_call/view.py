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
from bson.objectid import ObjectId
from app.Common.functionalities import insert_feeding_data_to_user


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

            post_data['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
            post_data['created_by'] = current_user
            post_data['_id'] = str(ObjectId())
            post_data['active'] = 1
            user_item = fire_call_model.RegisterCurb()
            user_item = user_item.insert_data(post_data)

            # call to feeding process fire_officer_and_team
            # feeding_resp = insert_feeding_data_to_user(post_data.get("fire_officer_and_team"), "fire_call")
            feeding_resp = insert_feeding_data_to_user(post_data['_id'], "fire_call")

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


@fire_cal.route('/approve')
# @jwt_required
class Login(Resource):
    """
         This class get form data
         @return: success or failure message
     """

    @fire_cal.expect(fire_call_serializers.approval, validate=True)
    @fire_cal.response(200, app.config["SUCCESS_MESSAGE_200"], fire_call_serializers.fire_call)
    @fire_cal.response(301, app.config["FAILURE_MESSAGE_301"], common_serializers.response_api_model)
    @fire_cal.response(400, app.config["FAILURE_MESSAGE_400"], common_serializers.response_api_model)
    @fire_cal.response(401, app.config["FAILURE_MESSAGE_401"], common_serializers.response_api_model)
    @fire_cal.response(403, app.config["FAILURE_MESSAGE_403"], common_serializers.response_api_model)
    @fire_cal.response(404, app.config["FAILURE_MESSAGE_404"], common_serializers.response_api_model)
    @fire_cal.response(409, app.config["FAILURE_MESSAGE_409"], common_serializers.response_api_model)
    @fire_cal.response(422, app.config["FAILURE_MESSAGE_422"], common_serializers.response_api_model)
    @fire_cal.response(500, app.config["FAILURE_MESSAGE_500"], common_serializers.response_api_model)
    def put(self):
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

            post_data['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
            post_data['updated_by'] = current_user
            id_number = post_data.get("_id")
            post_data['active'] = 1
            user_item = fire_call_model.RegisterCurb()
            user_item = user_item.find_modify({'_id': id_number}, post_data)

            more_info = "Successfully updated firecall data"
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


@fire_cal.route('/feeding_report')
# @jwt_required
class Login(Resource):
    """
         This class get form data
         @return: success or failure message
     """
    @fire_cal.expect(fire_call_serializers.feeding_report, validate=True)
    @fire_cal.response(200, app.config["SUCCESS_MESSAGE_200"], fire_call_serializers.feeding_report)
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
            post_data = request.get_json()
            from_date = post_data.get("from_date")
            to_date = post_data.get("to_date")
            user_item = fire_call_model.RegisterCurb()
            query = {
                "created_at":{
                    "$gt": f"{from_date}",
                    "$lt": f"{to_date}" 
                    }
                }

            user_item = user_item.get_feeding_info(query)

            more_info = "Successfully fetched firecall feeding report"
            return common_helpers.response('success',
                                           app.config["SUCCESS_MESSAGE_200"],
                                           more_info,
                                           user_item,
                                           200)
        except Exception as e:
            e = f"{traceback.format_exc()}"
            more_info = "Unable to fetch data :Exception occurred - " + str(e)
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)


