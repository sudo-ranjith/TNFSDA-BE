from flask import request
from flask_restplus import Resource, Namespace
import app.feeding_data.model as feeding_data_model
import app.feeding_data.serializers as feeding_data_serializers
from app import app
import app.Common.serializers as common_serializers
import app.Common.helpers as common_helpers
from datetime import  datetime
import traceback
from flask_jwt_simple import JWTManager, jwt_required, get_jwt_identity
from bson import json_util
from bson.objectid import ObjectId


feeding_ns = Namespace('feeding_data', description='fire man api')


@feeding_ns.route('/mail')
# @jwt_required
class Login(Resource):
    """
         This class get form data
         @return: success or failure message
     """

    @feeding_ns.expect(feeding_data_serializers.feeding_data, validate=True)
    @feeding_ns.response(200, app.config["SUCCESS_MESSAGE_200"], feeding_data_serializers.feeding_data)
    @feeding_ns.response(301, app.config["FAILURE_MESSAGE_301"], common_serializers.response_api_model)
    @feeding_ns.response(400, app.config["FAILURE_MESSAGE_400"], common_serializers.response_api_model)
    @feeding_ns.response(401, app.config["FAILURE_MESSAGE_401"], common_serializers.response_api_model)
    @feeding_ns.response(403, app.config["FAILURE_MESSAGE_403"], common_serializers.response_api_model)
    @feeding_ns.response(404, app.config["FAILURE_MESSAGE_404"], common_serializers.response_api_model)
    @feeding_ns.response(409, app.config["FAILURE_MESSAGE_409"], common_serializers.response_api_model)
    @feeding_ns.response(422, app.config["FAILURE_MESSAGE_422"], common_serializers.response_api_model)
    @feeding_ns.response(500, app.config["FAILURE_MESSAGE_500"], common_serializers.response_api_model)
    def post(self):
        try:
            if not (request.content_type == 'application/json'):
                return common_helpers.response('failed',
                                               app.config["FAILURE_MESSAGE_400"],
                                               'Content type should be application/json',
                                               [], 400)
            post_data = request.get_json()

            id_number = post_data.get("id_number")
            from_date = post_data.get("from_date")
            to_date = post_data.get("to_date")
           
            query = {
                "id_number": id_number,
                "created_at":{
                    "$gt": f"{from_date}",
                    "$lt": f"{to_date}" 
                    }
                }

            post_data['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
            post_data['_id'] = str(ObjectId())
            post_data['active'] = 1
            user_item = feeding_data_model.RegisterCurb()
            user_item = user_item.get_feeding_mail_data(query)
            if user_item.get('exists'):
                user_data = user_item['data']
                # send out email
                rescue_call_counter = 0
                fire_call_counter = 0
                mail_dict = {}
                for data in user_data:
                    mail_dict[data.get('id_number')] = {}
                    mail_dict[data.get('id_number')]['user_mail'] = data.get('email', 'sudo.ranjith@gmail.com')
                    mail_dict[data.get('id_number')]['user_name'] = data.get('first_name') + ' ' + data.get('last_name')
                    if data.get('call_type') == 'fire_call':
                        fire_call_counter += 1
                    if data.get('call_type') == 'rescue_call':
                        rescue_call_counter += 1

                    mail_dict[data.get('id_number')]['feeding_amount'] = len(user_data) * data.get('feeding_amount', 0)
                    mail_dict[data.get('id_number')]['feeding_report_month'] = f"{from_date} - {to_date}"
                mail_dict[data.get('id_number')]['fire_call_count'] = fire_call_counter
                mail_dict[data.get('id_number')]['rescue_call_count'] = rescue_call_counter
                common_helpers.sent_mail(mail_dict)
                more_info = "Successfully email sent"

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

@feeding_ns.route('/count')
# @jwt_required
class Login(Resource):
    """
         This class get form data
         @return: success or failure message
     """

    @feeding_ns.response(200, app.config["SUCCESS_MESSAGE_200"], feeding_data_serializers.feeding_data)
    @feeding_ns.response(301, app.config["FAILURE_MESSAGE_301"], common_serializers.response_api_model)
    @feeding_ns.response(400, app.config["FAILURE_MESSAGE_400"], common_serializers.response_api_model)
    @feeding_ns.response(401, app.config["FAILURE_MESSAGE_401"], common_serializers.response_api_model)
    @feeding_ns.response(403, app.config["FAILURE_MESSAGE_403"], common_serializers.response_api_model)
    @feeding_ns.response(404, app.config["FAILURE_MESSAGE_404"], common_serializers.response_api_model)
    @feeding_ns.response(409, app.config["FAILURE_MESSAGE_409"], common_serializers.response_api_model)
    @feeding_ns.response(422, app.config["FAILURE_MESSAGE_422"], common_serializers.response_api_model)
    @feeding_ns.response(500, app.config["FAILURE_MESSAGE_500"], common_serializers.response_api_model)
    def get(self):
        try:
            # post_data['created_by'] = current_user
            user_item = feeding_data_model.RegisterCurb()
            user_item = user_item.get_count()
            # user_item = json_util.dumps(user_item)

            more_info = "Successfully fetched feeding_ns count"
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

@feeding_ns.route('/feeding')
# @jwt_required
class Feeding(Resource):
    """
         This class get form data
         @return: success or failure message
     """

    @feeding_ns.response(200, app.config["SUCCESS_MESSAGE_200"], feeding_data_serializers.feeding_data)
    @feeding_ns.response(301, app.config["FAILURE_MESSAGE_301"], common_serializers.response_api_model)
    @feeding_ns.response(400, app.config["FAILURE_MESSAGE_400"], common_serializers.response_api_model)
    @feeding_ns.response(401, app.config["FAILURE_MESSAGE_401"], common_serializers.response_api_model)
    @feeding_ns.response(403, app.config["FAILURE_MESSAGE_403"], common_serializers.response_api_model)
    @feeding_ns.response(404, app.config["FAILURE_MESSAGE_404"], common_serializers.response_api_model)
    @feeding_ns.response(409, app.config["FAILURE_MESSAGE_409"], common_serializers.response_api_model)
    @feeding_ns.response(422, app.config["FAILURE_MESSAGE_422"], common_serializers.response_api_model)
    @feeding_ns.response(500, app.config["FAILURE_MESSAGE_500"], common_serializers.response_api_model)
    def post(self):
        try:
            user_item = feeding_data_model.RegisterCurb()
            user_item = user_item.get_count()
            """
            when feeding_ns completes his firecall
            input: id_number
            output: feeding info updated in feeding_ns name account successfully.
            find query-> fetch user data -> update feeding dict to user dict
            update in feeding collection
            {
                "username": "feeding_ns", feeding_amount:1000
            }

            """

            more_info = "Successfully fetched feeding_ns count"
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


@feeding_ns.route('/feeding_report')
# @jwt_required
class Login(Resource):
    """
         This class get form data
         @return: success or failure message
     """
    @feeding_ns.expect(feeding_data_serializers.feeding_report, validate=True)
    @feeding_ns.response(200, app.config["SUCCESS_MESSAGE_200"], feeding_data_serializers.feeding_report)
    @feeding_ns.response(301, app.config["FAILURE_MESSAGE_301"], common_serializers.response_api_model)
    @feeding_ns.response(400, app.config["FAILURE_MESSAGE_400"], common_serializers.response_api_model)
    @feeding_ns.response(401, app.config["FAILURE_MESSAGE_401"], common_serializers.response_api_model)
    @feeding_ns.response(403, app.config["FAILURE_MESSAGE_403"], common_serializers.response_api_model)
    @feeding_ns.response(404, app.config["FAILURE_MESSAGE_404"], common_serializers.response_api_model)
    @feeding_ns.response(409, app.config["FAILURE_MESSAGE_409"], common_serializers.response_api_model)
    @feeding_ns.response(422, app.config["FAILURE_MESSAGE_422"], common_serializers.response_api_model)
    @feeding_ns.response(500, app.config["FAILURE_MESSAGE_500"], common_serializers.response_api_model)
    def post(self):
        try:
            post_data = request.get_json()
            from_date = post_data.get("from_date")
            to_date = post_data.get("to_date")
            user_item = feeding_data_model.RegisterCurb()
           
            query = { "$match": {
                "created_at":{
                    "$gt": f"{from_date}",
                    "$lt": f"{to_date}" 
                    }
                }}

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
