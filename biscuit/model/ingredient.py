import sys
from biscuit.model.user import User
from biscuit.util.connection_helper import ConnectionHelper


class Ingredient():

    _id = None
    _name = None
    price_range = None

    def __init__(self, _name, _id):
        # NEVER call this
        self._id = _id
        self._name = _name


    # @classmethod
    # def create_ingredient(cls, conn, _name, _id):
    #     # Constructor (cls param is used for that)
    #     ingredient = Ingredient(_name, _id)
    #     #ingredient.insert_ingredient(conn, _name, _id)
    #     return ingredient


    @classmethod
    def get_ingredient(cls, conn, _id):
        # Constructor (cls param is used for that)

        ingredient_info = cls.query_with_id(cls, conn, _id)
        _id = ingredient_info[0]
        name = ingredient_info[1]
        ingredient = Ingredient(name, _id)
        return ingredient

    def query_with_id(self, conn, _id):
        query = 'SELECT * FROM ingredient WHERE id = %s'
        row = conn.run(query, _id)
        return row


    # def insert_ingredient(self, conn, _name, price_range):
    #     query = "INSERT INTO ingredient(_name, price_range)" \
    #             "VALUES (%s, %s)"
    #     args = (_name, price_range)
    #
    #     conn.run(query, args)
