import sys
from biscuit.model.user import User
from biscuit.util.connection_helper import ConnectionHelper


def get_pantries(conn, user_id):
    pass


def create_pantry_with_user(conn, pantry_name, user_id):
    pantry = Pantry.create_pantry(conn, pantry_name)
    pantry.associate_pantry(conn, user_id)
    return pantry

class Pantry():

    _id = None
    _name = None
    items = []

    def __init__(self, _name):
        # NEVER call this
        self._name = _name


    @classmethod
    def create_pantry(cls, conn, _name):
        # Constructor (cls param is used for that)
        pantry = Pantry(_name)
        pantry.insert_pantry(conn, _name)
        pantry.__update_id
        return pantry


    @classmethod
    def get_pantry(cls, conn, _id):
        # Constructor (cls param is used for that)
        self.query_with_id(conn, _id)


    def query_with_id(self, conn, _id):
        query = 'SELECT * FROM Pantry WHERE id = %s'
        try:
            cursor = conn.cursor()
            cursor.execute(query, _id)
            row = cursor.fetchone()
            print (row)

        except Exception as e:
            print(e)

        finally:
            cursor.close()


    def get_ingredients(self):
        return self.items

    def add_item(self, item_id, amount, unit):
        pass

    def insert_pantry(self, conn, _name):
        query = "INSERT INTO Pantry(_name)" \
                "VALUES (%s)"
        args = (_name)
        conn.run(query, args)

    def __update_id(self, conn):
        query = 'SELECT id FROM Pantry WHERE name=%s'
        self._id = conn.run(query, self._name)[0]

    def associate_pantry(self, conn, id_user):
        query = "INSERT INTO User_Pantry(id_user, id_pantry)" \
                "VALUES (%s, %s)"
        args = (id_user, self._id)

        try:
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()

        except Error as e:
            print(e)

        finally:
            cursor.close()
