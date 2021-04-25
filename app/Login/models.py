import traceback

from app import app, con
import app.Common.helpers as common_helpers
import mysql.connector


class LoginCurb:
    """
         This class insert data
         @author:
         @return: success or failure message
     """
    def read_data(self, query):
        try:
            con.ping(reconnect=True)
            sql_cur = con.cursor()
            sql_cur.execute(query)
            result_data = sql_cur.fetchone()
            if result_data:
                return {"exists": True, "item": result_data}
            return {"exists": False, "item": result_data}

        except Exception as e:
            more_info = "Unable to fetch data : Exception occurred - " + str(e)
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)
