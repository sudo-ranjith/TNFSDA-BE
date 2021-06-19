import traceback


def insert_feeding_data_to_user(id_number):
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