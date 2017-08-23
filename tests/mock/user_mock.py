ID = 42
NAME = 'Palmirinha'
EMAIL = 'palmirinha@hotmail.com'
PASSWORD = 'secreto.1234'
BIRTHDATE = '29/06/1931'


class User_Mock():

    _id = None
    name = None
    email = None
    password = None
    birthdate = None

    def __init__(self, conn, _id):
        self._id = _id
        self.name = NAME
        self.email = EMAIL
        self.password = PASSWORD
        self.birthdate = BIRTHDATE

    def __init__(self, conn, name, email, password, birthdate):
        self._id = ID
        self.name = name
        self.email = email
        self.password = password
        self.birthdate = birthdate
