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
check_format = "%Y-%m-%d"


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
        user_feeding_status = []
        for fire_men in fire_men_info:
            fireman_feeding_data = {}
            # check day_feeding_status
            one_fireman_data = fire_man_model.read_data({'id_number': fire_men.get('id_number')})
            one_fireman_data = one_fireman_data['data']
            user_feeding = feeding_model.read_data({'id_number': fire_men.get('id_number'), "accident_date": call_data.get('accident_date')})
            user_feeding = user_feeding['data']

            # if not one_fireman_data.get('total_feeding_amount'):
            #     one_fireman_data['total_feeding_amount'] = 0

            to_insert_data[f'call_id'] = id_number
            to_insert_data['feeding_amount'] = per_day_feeding_amount
            # to_insert_data['feeding_date'] = datetime.now().strftime(check_format)
            to_insert_data['feeding_date'] = call_data.get('accident_date')

            # insert feeding if fireman data was not in feeding data
            to_insert_data['day_feeding_status'] = "1"
            fireman_feeding_data['id_number'] = to_insert_data['id_number'] = fire_men.get('id_number')
            fireman_feeding_data['first_name'] = to_insert_data['first_name'] = one_fireman_data.get('first_name')
            fireman_feeding_data['last_name'] = to_insert_data['last_name'] = one_fireman_data.get('last_name')

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
                # one_fireman_data['total_feeding_amount'] = to_insert_data['total_feeding_amount'] = per_day_feeding_amount
                
                feeding_model.insert_data(to_insert_data)
                fire_man_model.find_modify({'id_number': fire_men.get('id_number')}, one_fireman_data)
                func_resp['status'] = "pass"
                func_resp['message'] = "feeding amount deposited."
                
            # check if fireman got feeding for the date,
            # if not updated feeding amount for today add existing total amount with per_day_feeding_amount

            elif user_feeding.get('feeding_date') and (user_feeding.get('feeding_date') != user_feeding.get('accident_date')):
                # to_insert_data['total_feeding_amount'] = one_fireman_data.get('total_feeding_amount') + per_day_feeding_amount
                # one_fireman_data['total_feeding_amount'] = to_insert_data['total_feeding_amount']
                
                feeding_model.insert_data(to_insert_data)
                fire_man_model.find_modify({'id_number': fire_men.get('id_number')}, one_fireman_data)
                func_resp['status'] = "pass"
                func_resp['message'] = "feeding amount deposited."

            else:
                # Incase if we want to provide feeding for some other purpose means, we can provide with day feeding flag.
                if user_feeding.get('day_feeding_status') == "0":
                    # insert data into feeding collection
                    # to_insert_data['total_feeding_amount'] = one_fireman_data.get('total_feeding_amount') + per_day_feeding_amount
                    # one_fireman_data['total_feeding_amount'] = to_insert_data['total_feeding_amount']
                    
                    feeding_model.insert_data(to_insert_data)
                    fire_man_model.find_modify({'id_number': fire_men.get('id_number')}, one_fireman_data)
                    func_resp['message'] = "feeding amount deposited."
                else:
                    func_resp['message'] = "already feeding amount deposited."    
            fireman_feeding_data['message'] = func_resp['message']
            user_feeding_status.append(fireman_feeding_data)
        func_resp['status'] = "pass"
    except Exception as e:
        func_resp['status'] = "fail"
        func_resp['error_details'] = traceback.format_exc()
        func_resp['message'] = f"oops got an exception in feeding amount process, Please contact system admin. Exception is {e}"
    finally:
        func_resp['user_feeding_status'] = user_feeding_status
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


def aggregate_user_data_with_feeding(monthly_feeding_data, query):
    func_resp = {}
    try:
        feeding_result = []
        rescue_call_data = rescue_call_model.read_all_data(query).get('data')
        fire_call_data = fire_call_model.read_all_data(query).get('data')
        fire_man_data = fire_man_model.read_all_data(query).get('data')
        
        for monthly_user_data in monthly_feeding_data:
            insertable_data = {}
            insertable_data["call_data"] = []
            # here will get each fire call, firemen data and append into a list
            temp_fireman_id = []
            for mnth_user_feed_records in monthly_user_data.get('records'):
                
                if mnth_user_feed_records.get('call_type') == 'fire_call':
                    for f_call_data in fire_call_data:
                    
                        if f_call_data.get('_id') == mnth_user_feed_records.get('call_id'):
                            # create each feeding row based on call
                            insertable_data["call_id"] = f_call_data.get('_id')
                            for fm_data in fire_man_data:
                                if fm_data.get('id_number') == mnth_user_feed_records.get('id_number'):
                                    if fm_data.get('id_number') in temp_fireman_id:
                                        # remove the existing data from the insertable list 
                                        insertable_data["call_data"].remove({"id_number": fm_data.get('id_number')})
                                        temp_fireman_id.append(fm_data.get('id_number'))
                                        insertable_data["call_data"].append(mnth_user_feed_records)
                                    else:
                                        temp_fireman_id.append(fm_data.get('id_number'))
                                        insertable_data["call_data"].append(mnth_user_feed_records)
                                else:
                                    fm_data['feeding_amount'] = "-"
                                    if (fm_data not in insertable_data["call_data"]) and (fm_data.get('id_number') not in temp_fireman_id):
                                        insertable_data["call_data"].append(fm_data)
                            # feeding_result.append(insertable_data)
                        else:
                            continue
                
                elif mnth_user_feed_records.get('call_type') == 'rescue_call':
                    # insertable_data = {}
                    # insertable_data["call_data"] = []
                    # temp_fireman_id = []
                    for r_call_data in rescue_call_data:
                        if r_call_data.get('_id') == mnth_user_feed_records.get('call_id'):
                            # create each feeding row based on call
                            insertable_data["call_id"] = r_call_data.get('_id')
                            for fm_data in fire_man_data:
                                if fm_data.get('id_number') == mnth_user_feed_records.get('id_number'):
                                    if fm_data.get('id_number') in temp_fireman_id:
                                        # remove the existing data from the insertable list
                                        insertable_data["call_data"].remove({"id_number": fm_data.get('id_number')})
                                        temp_fireman_id.append(fm_data.get('id_number'))
                                        insertable_data["call_data"].append(mnth_user_feed_records)
                                    else:
                                        temp_fireman_id.append(fm_data.get('id_number'))
                                        insertable_data["call_data"].append(mnth_user_feed_records)
                                else:
                                    fm_data['feeding_amount'] = "-"
                                    if (fm_data not in insertable_data["call_data"]) and (fm_data.get('id_number') not in temp_fireman_id):
                                        insertable_data["call_data"].append(fm_data)
                        else:
                            continue
            feeding_result.append(insertable_data)
        func_resp['status'] = "pass"

    except Exception:
        func_resp['message'] = traceback.format_exc()
        func_resp['status'] = "fail"
    finally:
        func_resp['data'] = feeding_result
        return func_resp


def generate_feeding_report(id_number):
    func_resp = {}
    try:
        func_resp['status'] = "pass"
    except Exception:
        func_resp['status'] = "fail"
    finally:
        return func_resp
