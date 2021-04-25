from app import app
import app.Common.helpers as common_helpers
import traceback
from app import mongo


class RegisterCurb:
    """
         This class insert data
         @author:
         @return: success or failure message
     """

    def insert_data(self, query):
        try:
            collection_name = app.config.get('REGISTRATION_COL')
            register_col = mongo.db.collection_name
            registered_email = register_col.insert_one(query)
            
        # to handle duplicate entry
        # except mysql.connector.IntegrityError as e:
        #     more_info = "Unable to Insert Duplicate entry " + traceback.format_exc()
        #     return common_helpers.response('failed',
        #                                    app.config["FAILURE_MESSAGE_409"],
        #                                    more_info, [], 400)

        # except mysql.connector.DatabaseError as e:
        #     more_info = "Unable to Inserted data : Exception occurred - DATABASE error" + traceback.format_exc()
        #     return common_helpers.response('failed',
        #                                    app.config["FAILURE_MESSAGE_500"],
        #                                    more_info, [], 500)
        except Exception as e:
            more_info = "Unable to Inserted data : Exception occurred - " + traceback.format_exc()
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)

    def read_data(self, query):
        try:
            collection_name = app.config.get('REGISTRATION_COL')
            register_col = mongo.db.collection_name
            result_data = register_col.find_one(query)
            print(result_data)
            if result_data:
                return {"exists": True, "item": result_data}
            return {"exists": False, "item": result_data}

        except Exception as e:
            more_info = "Unable to fetch data : Exception occurred - " + traceback.format_exc()
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)
