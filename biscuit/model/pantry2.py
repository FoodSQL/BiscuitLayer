import sys
from biscuit.model.user import User
from biscuit.util.connection_helper import ConnectionHelper


class Pantry():

    _id = None
    _name = None
    ingredients = []

    def __init__(self, _name):
        # NEVER call this
        self._name = _name
        self._id = None


    @classmethod
    def create_pantry(cls, conn, pantry_name, user_id):
        # Constructor (cls param is used for that)
        row = cls.insert_pantry(cls, conn, pantry_name)
        pantry = Pantry(pantry_name)
        pantry.update_id(conn)
        cls.associate_pantry(cls, conn, pantry._id, user_id)
        return pantry


    @classmethod
    def get_pantries(cls, conn, _id):
        # Constructor (cls param is used for that)
        pantry_info = cls.query_with_id(cls, conn, _id)
        lista = []
        for i in pantry_info:
            name = i[3]
            _id = i[2]
            pantry = Pantry(name)
            pantry._id = _id
            lista.append(pantry)
        return lista

    def add_ingredient(self, conn, ingredient):
        self.associate_ingredient(conn, ingredient._id)
        self.ingredients.append(ingredient)

    def remove_ingredient(self, conn, ingredient):
        query = "DELETE FROM ingredient_pantry WHERE id_ingredient = %s"
        conn.run(query, ingredient._id)
        for i in self.ingredients:
            if i._name == ingredient._name:
                self.ingredients.remove(i)

    def associate_ingredient(self, conn, ingredient_id):
        query = "INSERT INTO ingredient_pantry (id_ingredient, id_pantry)" \
                "VALUES (%s, %s)"
        args = (ingredient_id, self._id)
        conn.run(query, args)


    def query_with_id(self, conn, _id):
        query = 'SELECT * FROM User_Pantry up JOIN pantry p ON id_pantry = id WHERE id_user = %s'
        row = conn.runall(query, _id)
        return row


    def insert_pantry(self, conn, _name):
        query = "INSERT INTO pantry(_name)" \
                "VALUES (%s)"
        args = (_name)
        last = conn.run(query, args)
        print(last)

    def update_id(self, conn):
        query = 'SELECT id FROM Pantry WHERE _name=%s'
        self._id = conn.run(query, self._name)[0]


    def associate_pantry(self, conn, id_pantry, user_id):
        query = "INSERT INTO User_Pantry(id_user, id_pantry)" \
                "VALUES (%s, %s)"
        args = (user_id, id_pantry)

        conn.run(query, args)
