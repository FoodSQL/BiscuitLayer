import sys
from biscuit.model.user import User
from biscuit.util.connection_helper import ConnectionHelper


def get_pantries(conn, user_id):
    pass

class Pantry():

    _id = None
    _name = None

    def __init__(self, _name):
        # NEVER call this
        self._name = _name


    @classmethod
    def create_pantry(cls, conn, _name):
        # Constructor (cls param is used for that)
        pantry = Pantry(_name)
        pantry.insert_pantry(conn, _name)
        return pantry


    @classmethod
    def get_pantry(cls, conn, id):
        # Constructor (cls param is used for that)
        self.query_with_id(conn, id)


    def query_with_id(self, conn, id):
        query = 'SELECT * FROM Pantry WHERE id = %s'
        try:
            cursor = conn.cursor()
            cursor.execute(query, id)
            row = cursor.fetchone()
            print (row)

        except Exception as e:
            print(e)

        finally:
            cursor.close()

    def insert_pantry(self, conn, _name):
        query = "INSERT INTO Pantry(_name)" \
                "VALUES (%s)"
        args = (_name)
        conn.run(query, args)


    def associate_pantry(self, conn, id_panrty, email):
        user = User(conn, email)
        query = "INSERT INTO User_Pantry(id_user, id_pantry)" \
                "VALUES (%s, %s)"
        args = (user._id, id_pantry)

        try:
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()

        except Error as e:
            print(e)

        finally:
            cursor.close()
