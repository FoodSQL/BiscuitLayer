class Pantry_Mock():

    items = []
    _id = None
    _name = None


    def __init__(self, _id, _name, items):
        self._id = _id
        self._name = _name
        self.items = items


    def get_ingredients(self):
        return self.items
