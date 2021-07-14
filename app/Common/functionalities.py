import traceback
from app.feeding_data.model import RegisterCurb as feeding_model
from app.rescue_call.model import RegisterCurb as rescue_call_model
from app.fire_call.model import RegisterCurb as fire_call_model
from app.fire_man.model import RegisterCurb as fire_man_model
from datetime import datetime
from bson.objectid import ObjectId


feeding_model = feeding_model()
rescue_call_model = rescue_call_model()
fire_call_model = fire_call_model()
fire_man_model = fire_man_model()


per_day_feeding_amount = 250
check_format = "%Y%m%d"


def insert_feeding_data_to_user(id_number, call_type):
    func_resp = {}
    try:
        to_insert_data = {}
        to_insert_data['inserted_at'] = datetime.now()
        to_insert_data["call_type"] = call_type

        if call_type == 'fire_call':
            # get the number of fire man went to the call
            call_data = fire_call_model.read_data({'_id':id_number})
            call_data = call_data['data']
            fire_men_info = call_data.get('fire_officer_and_team')

        elif call_type == 'rescue_call':
            # get the number of fire man went to the call
            call_data = rescue_call_model.read_data({'_id':id_number})
            call_data = call_data['data']
            fire_men_info = call_data.get('fire_officer_and_team')

        for fire_men in fire_men_info:
            # check day_feeding_status
            one_fireman_data = fire_man_model.read_data({'id_number': fire_men.get('id_number')})
            one_fireman_data = one_fireman_data['data']
            user_feeding = feeding_model.read_data({'id_number': fire_men.get('id_number'), "feeding_date": datetime.now().strftime(check_format)})
            user_feeding = user_feeding['data']

            if not one_fireman_data.get('total_feeding_amount'):
                one_fireman_data['total_feeding_amount'] = 0

            to_insert_data[f'{call_type}_id'] = id_number
            to_insert_data['feeding_amount'] = per_day_feeding_amount
            to_insert_data['feeding_date'] = datetime.now().strftime(check_format)

            # insert feeding if fireman data was not in feeding data
            # check if fireman got feeding for the date,
            # if not updated feeding amount for today add existing total amount with per_day_feeding_amount
            to_insert_data['day_feeding_status'] = "1"
            to_insert_data['id_number'] = fire_men.get('id_number')
            to_insert_data['first_name'] = fire_men.get('first_name')
            to_insert_data['last_name'] = fire_men.get('last_name')

            to_insert_data['vehicle_start_time'] = call_data.get('vehicle_start_time')
            to_insert_data['vehicle_reached_time'] = call_data.get('vehicle_reached_time')
            to_insert_data['accident_date'] = call_data.get('accident_date')
            to_insert_data['created_at'] = call_data.get('created_at')
            to_insert_data['created_by'] = "admin"
            to_insert_data['update_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
            to_insert_data['update_by'] = "admin"
            to_insert_data['_id'] = str(ObjectId())

            if not user_feeding:
                # to_insert_data.get('total_feeding_amount') += per_day_feeding_amount
                one_fireman_data['total_feeding_amount'] = to_insert_data['total_feeding_amount'] = per_day_feeding_amount
                
                feeding_model.insert_data(to_insert_data)
                fire_man_model.find_modify({'id_number': fire_men.get('id_number')}, one_fireman_data)
                func_resp['status'] = "pass"
                
            elif user_feeding.get('feeding_date') and (user_feeding.get('feeding_date') != datetime.now().strftime(check_format)):
                to_insert_data['total_feeding_amount'] = one_fireman_data.get('total_feeding_amount') + per_day_feeding_amount
                one_fireman_data['total_feeding_amount'] = to_insert_data['total_feeding_amount']
                
                feeding_model.insert_data(to_insert_data)
                fire_man_model.find_modify({'id_number': fire_men.get('id_number')}, one_fireman_data)
                func_resp['status'] = "pass"

            else:
                if user_feeding.get('day_feeding_status') == "0":
                    # insert data into feeding collection
                    to_insert_data['total_feeding_amount'] = one_fireman_data.get('total_feeding_amount') + per_day_feeding_amount
                    one_fireman_data['total_feeding_amount'] = to_insert_data['total_feeding_amount']
                    
                    feeding_model.insert_data(to_insert_data)
                    fire_man_model.find_modify({'id_number': fire_men.get('id_number')}, one_fireman_data)
                else:
                    func_resp['message'] = "already feeding amount deposited."    

        func_resp['status'] = "pass"
    except Exception as e:
        func_resp['status'] = "fail"
        func_resp['error_details'] = traceback.format_exc()
        func_resp['message'] = f"oops got an exception in feeding amount process, Please contact system admin. Exception is {e}"
    finally:
        return func_resp


def insert_feeding_data_into_db(to_insert_data):
    # Insert in feeding table and update fireman table (feeding_amount)
    func_resp = {}
    try:
        func_resp['status'] = "pass"
    except Exception:
        func_resp['status'] = "fail"
    finally:
        return func_resp


def fetch_user_data(id_number):
    func_resp = {}
    try:
        func_resp['status'] = "pass"
    except Exception:
        func_resp['status'] = "fail"
    finally:
        return func_resp


def generate_feeding_report(id_number):
    func_resp = {}
    try:
        func_resp['status'] = "pass"
    except Exception:
        func_resp['status'] = "fail"
    finally:
        return func_resp
