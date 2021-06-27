# library imports
from flask_restplus import Resource, fields

# module imports
from app import api


login = api.model("login", {
    "id_number": fields.Integer(required=True, description="Enter id_number"),
    "rank": fields.String(required=True, description="Enter user RANK"),
    "password": fields.String(required=True, description="Enter password"),
})

