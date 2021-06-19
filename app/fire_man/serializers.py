# library imports
from flask_restplus import Resource, fields

# module imports
from app import api, fire_man


fire_man = api.model("fire_man", {
    "first_name" : fields.String(required=True, description="first_name"),
    "last_name" : fields.String(required=True, description="last_name"),
    "id_number" : fields.String(required=True, description="id_number"),
    "is_active" : fields.String(required=False, description="is fireman active"),
    'feeding_amount': fields.List(fields.Raw(), description="feeding_amount")
    })

