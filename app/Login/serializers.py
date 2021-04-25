from flask_restplus import Resource, fields
from app import api

# login model
login_api_model = api.model("login", {
    "civic_id": fields.String(required=True, description = "Enter user name for login"),
    "password": fields.String(required=True, description = "Enter the password"),
})

# login payload
login_payload = api.model('login payload', {
    'auth_token': fields.String,
    'refresh_token': fields.String,
    'user_id': fields.String
})
# login success
login_success_model = api.model("login success", {
   "status": fields.String(description="Status of the response - success or failure"),
   "message": fields.String(description="Message for the response - eg.Successfully registered"),
   "more_info": fields.String(description="More information about the response - mainly useful for error info"),
   "data": fields.Nested(login_payload, description="Retrieved data - if no data null is returned")
})

forget_password = api.model("forgot_password", {
   "email_civic_id": fields.String(description="Enter email or civic id"),
})
