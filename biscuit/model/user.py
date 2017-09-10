import sys


class User():

    _id = None
    name = None
    email = None
    password = None
    birthdate = None
    login = None

    def __init__(self, name=None, email=None, password=None, birthdate=None):
        # NEVER call this
        self.name = name
        self.email = email
        self.password = password
        self.birthdate = birthdate
        self.login = email


    @classmethod
    def create_user(cls, conn, name, email, password, birthdate):
        # Constructor (cls param is used for that)
        user = User(name, email, password, birthdate)
        user.insert_user(conn, name, email, password, birthdate)
        user.__update_id(conn)
        return user


    @classmethod
    def get_user(cls, conn, email):
        # Constructor (cls param is used for that)
        user = User()
        ans = user.query_with_email(conn, email)
        user._id = ans[0]
        user.name = ans[1]
        user.email = ans[2]
        user.password = ans[3]
        user.login = ans[4]
        user.birthdate = ans[5]
        return user


    @classmethod
    def get_user_by_id(cls, conn, _id):
        # Constructor (cls param is used for that)
        user = User()
        ans = user.query_with_id(conn, _id)
        user._id = ans[0]
        user.name = ans[1]
        user.email = ans[2]
        user.password = ans[3]
        user.login = ans[4]
        user.birthdate = ans[5]
        return user


    def __update_id(self, conn):
        query = 'SELECT id FROM _User WHERE login=%s'
        self._id = conn.run(query, self.login)[0]


    def query_with_id(self, conn, _id):
        query = 'SELECT * FROM _User WHERE id=%s'
        return conn.run(query, _id)


    def query_with_email(self, conn, email):
        query = 'SELECT * FROM _User WHERE login=%s'
        return conn.run(query, email)


    def insert_user(self, conn, name, email, password, birthdate):
        # Throws pymysql.err.IntegrityError if trying to create existing user
        query = "INSERT INTO _User(_name, login, _password, email)" +\
                "VALUES (%s, %s, %s, %s)"
        args = (name, email, password, email)
        print(conn.run(query, args))
