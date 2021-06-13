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
    "owner_name" : fields.String(required=True, description="owner_name"),
    "job" : fields.String(required=True, description="job"),
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
    "rescued_members" : fields.List(fields.Raw(), required=False, description="rescued_members"),
    "rescued_animal" : fields.String(required=False, description="rescued_animal"),
    "adipaadugal" : fields.String(required=True, description="adipaadugal"),
    "fire_station_name" : fields.String(required=True, description="fire_station_name"),
    "model_name" : fields.String(required=True, description="model_name"),
    "register_number" : fields.String(required=True, description="register_number"),
    "started_time" : fields.String(required=True, description="started_time"),
    "reached_ime" : fields.String(required=True, description="reached_ime"),
    "return_time" : fields.String(required=True, description="return_time"),
    "reached_station_time" : fields.String(required=True, description="reached_station_time"),
    "travel_hours" : fields.String(required=True, description="travel_hours"),
    "water_pumbing_time" : fields.String(required=True, description="water_pumbing_time"),
    })

