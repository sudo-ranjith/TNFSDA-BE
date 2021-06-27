# library imports
from flask_restplus import Resource, fields

# module imports
from app import api


login = api.model("login", {
    "id_number": fields.String(required=True, description="Enter id_number"),
    "password": fields.String(required=True, description="Enter password"),
})

