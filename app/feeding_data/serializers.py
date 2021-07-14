# library imports
from flask_restplus import Resource, fields

# module imports
from app import api, feeding_data


feeding_data = api.model("feeding_data", {
    "id_number" : fields.String(required=True, description="id_number"),
    "feeding_amount" : fields.String(required=True, description="feeding_amount"),

    "is_active" : fields.String(required=True, description="is fireman active"),
    'feeding_history': fields.List(fields.Raw(), description="feeding_history")
    })


feeding_report = api.model("feeding_report", {
    'from_date': fields.String(required=True, description="from_date"),
    'to_date': fields.String(required=True, description="to_date")
    })