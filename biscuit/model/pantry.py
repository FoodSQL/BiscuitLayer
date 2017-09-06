class Pantry():

    _id = None
    name = None

    def create_pantry(self, name):


    def insert_pantry(self, conn, name):
        query = "INSERT INTO Pantry(_name)" \
                "VALUES (%s)"
        args = (name)

        try:
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()

        except Error as e:
            print(e)

        finally:
            cursor.close()

    def get_user_id(self, conn, email):
        query = 'SELECT id FROM _user WHERE email = %s'

        try:
            cursor = conn.cursor()
            cursor.execute(query, args)
            print (cursor.fetchone())
            conn.commit()

        except Error as e:
            print(e)

        finally:
            cursor.close()

    def associate_pantry(self, conn, id, email):



        query = "INSERT INTO User_Pantry(id_user)" \
                "VALUES (%s)"
        args = (name)

        try:
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()

        except Error as e:
            print(e)

        finally:
            cursor.close()
