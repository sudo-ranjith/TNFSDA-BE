from flask import jsonify
from app import app, mail
import smtplib, ssl
from email.mime.text import MIMEText
from email.message import EmailMessage


def response(status, message, more_info, data, code, token=''):
    """
    Method to generate response
    """
    return_response = jsonify({
        'status': status,
        'message': message,
        'more_info': more_info,
        'data': data,
        'token': token
    })
    return_response.status_code = code
    return return_response


def response_json(status, message, more_info, data, code):
    """
    Method to generate response json
    """
    return_response = {
        'status': status,
        'message': message,
        'more_info': more_info,
        'data': data,
        'status_code': code
    }
    return return_response


def response_jsonify(response_obj):
    """
    Method to generate response
    """
    return_response = jsonify({
        'status': response_obj["status"],
        'message': response_obj["message"],
        'more_info': response_obj["more_info"],
        'data': response_obj["data"]
    })
    return_response.status_code = response_obj["status_code"]
    return return_response


def response_jsonify(response_obj):
    """
    Method to generate response
    """
    return_response = jsonify({
        'status': response_obj["status"],
        'message': response_obj["message"],
        'more_info': response_obj["more_info"],
        'data': response_obj["data"]
    })
    return_response.status_code = response_obj["status_code"]
    return return_response


def sent_mail(email, password):

    message = """\
    Hi ,
    user_name - {}
    password  - {}""".format(email, password)
    msg = EmailMessage()
    msg['Subject'] = 'Login Credentials'
    msg['From'] = app.config["MAIL_USERNAME"]
    msg['To'] = email
    msg.set_content(message)
    server = smtplib.SMTP_SSL(app.config["MAIL_SERVER"], app.config["MAIL_PORT"])
    server.login(app.config["MAIL_USERNAME"], app.config["MAIL_PASSWORD"])
    server.send_message(msg)
    server.quit()
