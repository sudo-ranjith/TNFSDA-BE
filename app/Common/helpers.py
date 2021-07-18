import traceback
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


def sent_mail(mail_dict):
    func_resp = {}
    try:
        key_name = mail_dict.keys()
        for _key in key_name:
            user_name = mail_dict[_key]['user_name']
            fire_call_count = mail_dict[_key].get('fire_call_count', 0)
            rescue_call_count = mail_dict[_key].get('rescue_call_count', 0)
            feeding_amount = mail_dict[_key]['feeding_amount']
            feeding_report_month = mail_dict[_key]['feeding_report_month']
            message = f"""\
            வணக்கம் {user_name},
                நீங்கள் {feeding_report_month} நாட்களில் {fire_call_count} தீயணைப்பு மற்றும் {rescue_call_count} மீட்புப் பணியில் சிறப்பாக பணி ஆற்றியமைக்கு வாழ்த்துகள்.
            அதற்காக தங்களுக்கு ஒதுக்கப்பட்ட மாத உணவுபடி ரூபாய் {feeding_amount}."""
            msg = EmailMessage()
            msg['Subject'] = f'Feeding Report of {feeding_report_month}'
            msg['From'] = app.config["MAIL_USERNAME"]
            msg['To'] = mail_dict[_key]['user_mail']
            msg.set_content(message)
            server = smtplib.SMTP_SSL(app.config["MAIL_SERVER"], app.config["MAIL_PORT"])
            server.login(app.config["MAIL_USERNAME"], app.config["MAIL_PASSWORD"])
            server.send_message(msg)
            server.quit()

    except Exception as e:
        func_resp['message'] = traceback.format_exc()
        func_resp['status'] = "failed"
    finally:
        return func_resp
