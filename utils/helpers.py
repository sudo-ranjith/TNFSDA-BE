from datetime import datetime
from flask import jsonify
from time import time


# REF: https://www.geeksforgeeks.org/decorators-in-python/
def calculate_proc_time(job):
    def _wrap(*args, **kwargs):
        proc_start = time()
        func_resp = job(*args, **kwargs)
        proc_end = time()
        func_resp["time_stamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        func_resp["run_time"] = f"{proc_end - proc_start:.2f} seconds"
        return jsonify(func_resp)
    return _wrap
