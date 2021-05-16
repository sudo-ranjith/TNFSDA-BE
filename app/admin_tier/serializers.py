# library imports
from flask_restplus import Resource, fields

# module imports
from app import api


login = api.model("login", {
    "email": fields.String(required=True, description="Enter email"),
    "rank": fields.Integer(required=True, description="Enter user RANK"),
    "kottam": fields.String(required=True, description="Enter kottam")
    })

