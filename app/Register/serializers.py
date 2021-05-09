# library imports
from flask_restplus import Resource, fields

# module imports
from app import api


register = api.model("register", {
    "username": fields.String(required=True, description="Enter username"),
    "email": fields.String(required=True, description="Enter email_address"),
    "mobile": fields.Integer(required=True, description="Enter phone_number"),
    "rank": fields.Integer(required=True, description="Enter user RANK"),
    "password": fields.String(required=True, description="Enter password"),
})

