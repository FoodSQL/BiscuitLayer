import sys
from biscuit.model.user import User
from biscuit.util.connection_helper import ConnectionHelper

class DAO():

    def __init__(self, conn):
        self.conn = conn


    def return_all_user_pantries(self, user_id):
        return query_with_id(self, user_id)
        

    def query_with_id(self, conn, id):
        query = 'SELECT * FROM user_pantry WHERE id = %s'
        cursor.run(query, id)
        row = fetchall()
        return row
