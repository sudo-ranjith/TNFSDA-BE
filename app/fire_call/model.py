from app import app
import app.Common.helpers as common_helpers
import traceback
from app import mongo
from pymongo import ReturnDocument


class RegisterCurb:
    """
         This class insert data
         @author:
         @return: success or failure message
     """
    
    def __init__(self):
        # assigning collection name here
        self.fire_call_col = mongo.db.fire_call
        

    def insert_data(self, query):
        try:
            registered_email = self.fire_call_col.insert_one(query)
            
        except Exception as e:
            more_info = "Unable to Inserted data : Exception occurred - " + traceback.format_exc()
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)

    def get_count(self):
        try:
            user_info = self.fire_call_col.find({})
            user_info = list(user_info)
            more_info = "Unable to Inserted data : Exception occurred - " + traceback.format_exc()
            return {"data": user_info, "count": len(user_info)}
            
        except Exception as e:
            more_info = "Unable to Inserted data : Exception occurred - " + traceback.format_exc()
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)


    def read_data(self, query):
        try:
            result_data = self.fire_call_col.find_one(query)
            print(result_data)
            if result_data:
                return {"exists": True, "data": result_data}
            return {"exists": False, "data": result_data}

        except Exception as e:
            more_info = "Unable to fetch data : Exception occurred - " + traceback.format_exc()
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)

    def get_feeding_info(self, query):
        try:
            projection = {
                "vehicle_start_time": 1,
                "vehicle_reached_time": 1,
                "fire_officer_and_team": 1,
                "accident_date": 1
            }
            result_data = self.fire_call_col.find(query, projection)
            print(result_data)
            if result_data:
                return {"exists": True, "data": list(result_data)}
            return {"exists": False, "data": result_data}

        except Exception as e:
            more_info = "Unable to fetch data : Exception occurred - " + traceback.format_exc()
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)

    def find_modify(self, query, update):
        try:
            result_data = self.fire_call_col.find_one_and_update(query,{'$set':update}, return_document = ReturnDocument.AFTER)
            print(result_data)
            if result_data:
                return {"exists": True, "data": result_data}
            return {"exists": False, "data": result_data}

        except Exception as e:
            more_info = "Unable to fetch data : Exception occurred - " + traceback.format_exc()
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)

