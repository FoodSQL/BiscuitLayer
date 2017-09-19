import sys
from biscuit.model.user import User
from biscuit.util.connection_helper import ConnectionHelper
from biscuit.model.pantry2 import Pantry

class Recipe():

    _id = None
    _name = None
    description = None
    difficulty = None
    ingredients = None


    def __init__(self, _id, name, description, difficulty, ingredients):
        self._id = _id
        self._name = _name
        self.description = description
        self.difficulty = difficulty
        self.ingredients = ingredients

    @classmethod
    def create_recipe():
        pass

    @classmethod
    def get_recipe_by_id(cls, conn, _id):
        query = "SELECT * FROM Recipe JOIN Recipe_Ingredient ON id_recipe = _id WHERE _id = %s"
        result = conn.run(query, _id)
        _id = result[0]
        _name = result[1]



    @classmethod
    def get_recipes_by_ingredient(cls, conn, pantry_id):
        pantry = pantry.get_pantry(conn, pantry_id)


        query = '''
                    select
                        Recipe._name as recipe_name,
                        Ingredient._name as ingredient_name
                    from
                        Recipe
                    inner join Recipe_Ingredient
                        on Recipe.id = Recipe_Ingredient.id_recipe
                    inner join Ingredient
                        on Ingredient.id = Recipe_Ingredient.id_ingredient
                    inner join Ingredient_Pantry
                        on Ingredient.id = Ingredient_Pantry.id_ingredient
                    inner join Pantry
                        on Ingredient_Pantry.id_pantry = Pantry.id
                    where
                        Ingredient.id = (%s)
                '''
        for i in pantry.get_ingredients:
            print(conn.runall(query, i))

        print(conn.runall(query))
        # recipes.append(recipe)

        return recipes
