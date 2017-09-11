import pymysql

from pathlib import Path  # sql config file


class ConnectionHelper:

    def __init__(self, connection=None):
        if connection:
            self.connection = pymysql.connect(connection)
        else:
            self.connection = pymysql.connect(**ConnectionHelper
                                              .__get_connection_options())


    def run(self, query, args=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, args)
            result = cursor.fetchone()
        self.connection.commit()
        return result

    def runall(self, query, args=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, args)
            result = cursor.fetchall()
        self.connection.commit()
        return result


    def __get_connection_options():
        database = 'my_chef'
        try:
            home = str(Path.home())
            with open('/{}/mysql-keys.txt'.format(home), 'r') as f:
                host = str(f.readline().strip())
                user = str(f.readline().strip())
                password = str(f.readline().strip())

        except:
            host = 'localhost'
            user = 'root'
            password = '1234'

        finally:
            conn_opt = {
                'host': "localhost",
                'user': "root",
                'password': "Derrick1",
                'database': "my_chef",
            }
            return conn_opt
