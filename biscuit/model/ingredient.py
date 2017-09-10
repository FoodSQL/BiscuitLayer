import sys
from biscuit.model.user import User
from biscuit.util.connection_helper import ConnectionHelper


class Ingredient():

    _id = None
    _name = None
    price_range = None

    def __init__(self, _name, price_range):
        # NEVER call this
        self._name = _name
        self.price_range = price_range


    @classmethod
    def create_ingredient(cls, conn, _name, price_range):
        # Constructor (cls param is used for that)
        ingredient = Ingredient(_name, price_range)
        ingredient.insert_ingredient(conn, _name, price_range)
        return ingredient


    @classmethod
    def get_ingredient(cls, conn, id):
        # Constructor (cls param is used for that)
        print(self.query_with_id(conn, id))


    def query_with_id(self, conn, id):
        query = 'SELECT * FROM ingredient WHERE id = %s'
        cursor.run(query, id)
        return row


    def insert_ingredient(self, conn, _name, price_range):
        query = "INSERT INTO ingredient(_name, price_range)" \
                "VALUES (%s, %s)"
        args = (_name, price_range)

        conn.run(query, args)
