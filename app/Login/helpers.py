from datetime import datetime, timedelta

from flask import jsonify

import app.Common.helpers as common_helpers

import jwt

from app import app


def response(status, message, more_info, data, status_code):
    """
    Method to generate response of login with auth token and user id
    """
    data["auth_token"] = data["auth_token"].decode("utf-8")
    return_response = jsonify({
        "status": status,
        "message": message,
        'more_info': more_info,
        'data': data
    })
    return_response.status_code = status_code
    return return_response


def encode_auth_token(user_id, tenant_id):
    """
    Method to encode jwt token
    """
    try:
        payload = {
            'user_id': user_id,
            'tenant_id': tenant_id
        }
        encoded_token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
        return encoded_token

    except Exception as e:
        more_info = "Unable to encode auth token : Exception occurred -"+str(e)
        return common_helpers.response('failed',
                                        app.config["FAILURE_MESSAGE_500"],
                                        more_info, [], 500)
