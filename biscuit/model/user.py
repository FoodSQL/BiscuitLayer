import sys


class User():

    _id = None
    name = None
    email = None
    password = None
    birthdate = None

    def __init__(self, name, email, password, birthdate):
        # NEVER call this
        self.name = name
        self.email = email
        self.password = password
        self.birthdate = birthdate


    @classmethod
    def create_user(cls, conn, name, email, password, birthdate):
        # Constructor (cls param is used for that)
        user = User(name, email, password, birthdate)
        user.insert_user(conn, name, email, password, birthdate)
        return user


    @classmethod
    def get_user(cls, conn, email):
        # Constructor (cls param is used for that)
        self.query_with_id(conn, email)


    def query_with_id(self, conn, email):
        query = 'SELECT * FROM _user WHERE email = %s'
        try:
            cursor = conn.cursor()
            cursor.execute(query, email)
            row = cursor.fetchone()
            print (row)

        except Exception as e:
            print(e)

        finally:
            cursor.close()

    def insert_user(self, conn, name, email, password, birthdate):
        query = "INSERT INTO _User(_name, login, _password, email)" \
                "VALUES (%s, %s, %s, %s)"
        args = (name, email, password, email)
        conn.run(query, args)
