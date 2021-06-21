import traceback
from app.feeding_data.model import RegisterCurb as feeding_model
from app.fire_call.model import RegisterCurb as fire_call_model
from datetime import datetime


per_day_feeding_amount = 250
check_format = "%Y%m%d"


def insert_feeding_data_to_user(id_number, call_type):
    func_resp = {}
    try:
        to_insert_data = {}
        to_insert_data['inserted_at'] = datetime.now()
        # get the number of fire man went to the call
        fire_call_data = fire_call_model.read_data({'_id':id_number})
        fire_men_info = fire_call_data.get('fire_officer_and_team')
        for fire_men in fire_men_info:
            # check day_feeding_status
            user_feeding = feeding_model.read_data({'id_number': fire_men.get('id_number')})

            to_insert_data[f'{call_type}_id'] = id_number
            to_insert_data['feeding_amount'] = 250
            to_insert_data['feeding_date'] = datetime.now().strftime(check_format)

            if not user_feeding.get('exists'):
                to_insert_data['total_amount'] = 250
                to_insert_data['day_feeding_status'] = "1"
                to_insert_data['id_number'] = fire_men.get('id_number')

                feeding_model.insert_data(to_insert_data)
                func_resp['status'] = "pass"
                return func_resp
            
            else:
                if user_feeding.get('day_feeding_status') == "0":
                    # insert data into feeding collection
                    feeding_model.insert_data(to_insert_data)

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