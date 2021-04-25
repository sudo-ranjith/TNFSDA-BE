from flask import request
from flask_restplus import Resource, Namespace
import app.Register.model as register_model
import app.Register.serializers as register_serializers
from app import app
import app.Common.serializers as common_serializers
import app.Common.helpers as common_helpers
from datetime import  datetime


register = Namespace('Register', description='Registration')


@register.route('')
class Register(Resource):
    """
         This class get form data
         @return: success or failure message
     """

    @register.expect(register_serializers.register, validate=True)
    @register.response(200, app.config["SUCCESS_MESSAGE_200"], register_serializers.register)
    @register.response(301, app.config["FAILURE_MESSAGE_301"], common_serializers.response_api_model)
    @register.response(400, app.config["FAILURE_MESSAGE_400"], common_serializers.response_api_model)
    @register.response(401, app.config["FAILURE_MESSAGE_401"], common_serializers.response_api_model)
    @register.response(403, app.config["FAILURE_MESSAGE_403"], common_serializers.response_api_model)
    @register.response(404, app.config["FAILURE_MESSAGE_404"], common_serializers.response_api_model)
    @register.response(409, app.config["FAILURE_MESSAGE_409"], common_serializers.response_api_model)
    @register.response(422, app.config["FAILURE_MESSAGE_422"], common_serializers.response_api_model)
    @register.response(500, app.config["FAILURE_MESSAGE_500"], common_serializers.response_api_model)
    def post(self):
        try:
            if not (request.content_type == 'application/json'):
                return common_helpers.response('failed',
                                               app.config["FAILURE_MESSAGE_400"],
                                               'Content type should be application/json',
                                               [], 400)
            post_data = request.get_json()
            username = post_data.get("username")
            email = post_data.get("email")
            mobile = post_data.get("mobile")
            password = post_data.get("password")
            rank = post_data.get("rank")

            check_existing_query = {"email":  email}

            registeration_obj = register_model.RegisterCurb()
            check_existing_details = registeration_obj.read_data(check_existing_query)
            if check_existing_details["exists"]:
                more_info = "Already exists {}".format(check_existing_details)
                return common_helpers.response('failed', app.config["FAILURE_MESSAGE_409"],
                                            more_info,
                                            [], 409)

            post_data['created_at'] = datetime.now().strftime('%Y%m%d%H%M%S%f')
            post_data['active'] = 1
            user_item = register_model.RegisterCurb()
            user_item = user_item.insert_data(post_data)

            if user_item is not None:
                return user_item
            user_item = register_model.RegisterCurb()
            more_info = "Successfully Inserted"
            return common_helpers.response('success',
                                           app.config["SUCCESS_MESSAGE_200"],
                                           more_info,
                                           [],
                                           200)
        except Exception as e:
            more_info = "Unable to Inserted data :Exception occurred - " + str(e)
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)