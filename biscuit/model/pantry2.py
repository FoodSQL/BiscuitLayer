import sys
from user import User


class Pantry():

    _id = None
    name = None

    def __init__(self, name):
        # NEVER call this
        self.name = name


    @classmethod
    def create_pantry(cls, conn, name):
        # Constructor (cls param is used for that)
        pantry = Pantry(name)
        pantry.insert_pantry(conn, name)
        return pantry


    @classmethod
    def get_pantry(cls, conn, id):
        # Constructor (cls param is used for that)
        self.query_with_id(conn, id)


    def query_with_id(self, conn, id):
        query = 'SELECT * FROM _pantry WHERE id = %s'
        try:
            cursor = conn.cursor()
            cursor.execute(query, id)
            row = cursor.fetchone()
            print (row)

        except Exception as e:
            print(e)

        finally:
            cursor.close()

    def insert_pantry(self, conn, name):
        query = "INSERT INTO _pantry(_name)" \
                "VALUES (%s)"
        args = (name)
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
