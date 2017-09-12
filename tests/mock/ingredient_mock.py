class Ingredient_Mock():

    _id = None
    _name = None
    amount = None
    unit = 'kg'


    def __init__(self, _id, _name, _amount):
        self._id = _id
        self._name = _name
        self.amount = _amount
