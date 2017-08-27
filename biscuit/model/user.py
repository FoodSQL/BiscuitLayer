class User():

    _id = None
    name = None
    email = None
    password = None
    birthdate = None

    def create_user(self, conn, name, email, password, birthdate):
        self.name = name
        self.email = email
        self.password = email
        self.birthdate = birthdate
        self.insert_user(conn, name, email, password, birthdate)

    def get_user(self, conn, email):
        self.query_with_id (conn, email)


    def query_with_id(self, conn, email):
        query = 'SELECT * FROM _user WHERE email = %s'
        try:
            cursor = conn.cursor()
            cursor.execute(query, email)

            row = cursor.fetchone()

            print (row)

        except Error as e:
            print(e)

        finally:
            cursor.close()

    def insert_user(self, conn, name, email, password, birthdate):
        query = "INSERT INTO _User(_name, login, _password, email, birthdate)" \
                "VALUES (%s, %s, %s, %s, %s)"
        args = (name, email, password, email, birthdate)

        try:
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()

        except Error as e:
            print(e)

        finally:
            cursor.close()
