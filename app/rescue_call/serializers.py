# library imports
from flask_restplus import Resource, fields

# module imports
from app import api


rescue_call = api.model("rescue_call", {
    "kottam" : fields.String(required=True, description="kottam"),
    "station" : fields.String(required=True, description="station"),
    "fire_officer_name" : fields.String(required=True, description="fire_officer_name"),
    "arikkai_number" : fields.String(required=True, description="arikkai_number"),
    "accident_date" : fields.String(required=True, description="accident_date"),
    "caller_name" : fields.String(required=True, description="caller_name"),
    "telephone_number" : fields.String(required=True, description="telephone_number"),
    "accident_address" : fields.String(required=True, description="accident_address"),
    "AllInOnePerson" : fields.String(required=True, description="AllInOnePerson"),
    "owner_name" : fields.String(required=True, description="owner_name"),
    "occupation" : fields.String(required=True, description="occupation"),
    "owner_name_address" : fields.String(required=True, description="owner_name_address"),
    "calling_time" : fields.String(required=True, description="calling_time"),
    "vehicle_start_time" : fields.String(required=True, description="vehicle_start_time"),
    "vehicle_reached_time" : fields.String(required=True, description="vehicle_reached_time"),
    "between_distance" : fields.String(required=True, description="between_distance"),
    "incident_time" : fields.String(required=True, description="incident_time"),
    "detail_about_incident" : fields.String(required=True, description="detail_about_incident"),
    "reason_fortheincident": fields.String(required=True, description="Enter reason_fortheincident"), 
    "rescue_work" : fields.String(required=True, description="rescue_work"),
    "last_return_officer" : fields.String(required=True, description="last_return_officer"),
    "return_date_time_from_fire_acc" : fields.String(required=True, description="return_date_time_from_fire_acc"),
    "fire_controlling_time" : fields.String(required=True, description="fire_controlling_time"),
    "type" : fields.String(required=True, description="type"),
    "rescued_animal_active" : fields.String(required=True, description="rescued_animal_active"),
    "type_of_animal" : fields.String(required=True, description="type_of_animal"),
    "no_of_animal" : fields.String(required=True, description="no_of_animal"),
    "approve_status" : fields.Integer(required=True, description="approve_status"),

    "escaped_or_rescued_active" : fields.String(required=True, description="escaped_or_rescued_active"),
    "escaped_or_rescued" : fields.List(fields.Raw(), required=False, description="rescued_members"),
    'arrive_and_act': fields.List(fields.Raw(), description="arrive_and_act"),
    "adipaadugal_active" : fields.String(required=True, description="adipaadugal_active"),
    'adipadugal_fire': fields.List(fields.Raw(), description="adipadugal_fire"),
    'adipadugal_others': fields.List(fields.Raw(), description="adipadugal_others"),
    'fire_officer_and_team':fields.List(fields.Raw(), description="fire_officer_and_team"),

    'Others': fields.String(required=True, description="Others"),
    'Sign': fields.String(required=True, description="Sign")
    })

approval = api.model("approval", {
    "approve_status" : fields.Integer(required=True, description="approval"),
    '_id': fields.String(required=True, description="_id")
    })
