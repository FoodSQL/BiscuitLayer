import sys
from biscuit.model.user import User
from biscuit.util.connection_helper import ConnectionHelper


def get_all_ingredients(conn):
    pass

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

    @classmethod
    def get_all_ingredients(cls, conn):
        query = ("SELECT * FROM Ingredient")
        result = conn.runall(query)
        ingredients_list = []
        for i in result:
            _id = i[0]
            name = i[1]
            ingredient = Ingredient(name, _id)
            ingredients_list.append(ingredient)
        return ingredients_list

    def query_with_id(self, conn, id):
        query = 'SELECT * FROM Ingredient WHERE id = %s'
        row = conn.run(query, id)
        print (row)
        return row


    def insert_ingredient(self, conn, _name, price_range):
        query = "INSERT INTO Ingredient(_name, price_range)" \
                "VALUES (%s, %s)"
        args = (_name, price_range)

        conn.run(query, args)
