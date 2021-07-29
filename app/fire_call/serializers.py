# library imports
from flask_restplus import Resource, fields

# module imports
from app import api, fire_call


fire_call = api.model("fire_call", {
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
    # "type_of_fire" : fields.String(required=False, description="type_of_fire"),
    "area_of_fire" : fields.String(required=True, description="area_of_fire"),
    "destruction_details" : fields.String(required=True, description="destruction_details"),
    "accidental_possession" : fields.String(required=True, description="accidental_possession"),
    "any_risk_at_surroundings" : fields.String(required=True, description="any_risk_at_surroundings"),
    "destruction_of_the_site" : fields.String(required=True, description="destruction_of_the_site"),
    "dstrctn_for_those_who_within" : fields.String(required=True, description="dstrctn_for_those_who_within"),
    "value_of_property_protected_by_fire" : fields.String(required=True, description="value_of_property_protected_by_fire"),
    "approve_status" : fields.Integer(required=True, description="approval"),

    "escaped_or_rescued_active" : fields.String(required=False, description="escaped_or_rescued_active"),
    "escaped_or_rescued" : fields.List(fields.Raw(), description="rescued_members"),
    'arrive_and_act': fields.List(fields.Raw(), description="arrive_and_act"),
    "adipaadugal_active" : fields.String(required=False, description="adipaadugal_active"),
    'adipadugal_fire': fields.List(fields.Raw(), description="adipadugal_fire"),
    'adipadugal_others': fields.List(fields.Raw(), description="adipadugal_others"),
    'fire_officer_and_team':fields.List(fields.Raw(), description="fire_officer_and_team"),

    'Others': fields.String(required=False, description="Others"),
    'Sign': fields.String(required=True, description="Sign")
    })


approval = api.model("approval", {
    "approve_status" : fields.Integer(required=True, description="approval"),
    '_id': fields.String(required=True, description="_id")
    })


feeding_report = api.model("feeding_report", {
    'from_date': fields.String(required=True, description="from_date"),
    'to_date': fields.String(required=True, description="to_date")
    })