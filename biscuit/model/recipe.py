import sys
from biscuit.model.user import User
from biscuit.util.connection_helper import ConnectionHelper
from biscuit.model.pantry2 import Pantry
from biscuit.model.ingredient import Ingredient

class Recipe():

    _id = None
    _name = None
    description = None
    difficulty = None
    ingredients = []
    percentage = None


    def __init__(self, _id, name, description, difficulty=None, ingredients=None):
        self._id = _id
        self._name = name
        self.description = description
        self.difficulty = difficulty
        self.ingredients = []
        self.percentage = None

    @classmethod
    def create_recipe():
        pass

    @classmethod
    def get_recipe_by_id(cls, conn, _id):
        query = """SELECT Recipe._name, Recipe.id FROM Recipe
                JOIN Recipe_Ingredient ON id_recipe = Recipe.id
                JOIN Ingredient ON id_ingredient = Ingredient.id
                WHERE Recipe.id = %s"""
        result = conn.run(query, _id)
        _id = result[1]
        _name = result[0]
        recipe = Recipe(_id, _name, _name)
        recipe.get_recipe_ingredients(conn)
        return recipe


    def get_recipe_ingredients(self, conn):
        query = """
            SELECT i._name, i.id, ri.id_recipe
            FROM Recipe_Ingredient as ri
            JOIN Ingredient as i
            ON i.id = ri.id_ingredient
            WHERE ri.id_recipe = %s
        """

        result = conn.runall(query, self._id)
        for i in result:
            ingredient = Ingredient(i[0], i[1])
            self.ingredients.append(ingredient)


    @classmethod
    def get_recipes_by_ingredient(cls, conn, pantry_id):
        pantry = Pantry.get_pantry(conn, pantry_id)

        delete_view = 'DROP VIEW IF EXISTS ing_num;'
        create_view =  '''
            START TRANSACTION;
            CREATE VIEW ing_num  AS
            SELECT r._name as _name, r.id as _id, COUNT(ri.id_recipe)  as rec_num
            FROM Recipe_Ingredient AS ri
            INNER JOIN Recipe AS r
            ON id = id_recipe
            GROUP BY ri.id_recipe;
        '''
        mega_join = '''
            select
                Recipe._name as recipe_name,
                Ingredient._name as ingredient_name,
                Recipe.id,
                COUNT(Recipe.id),
                COUNT(Ingredient.id)/ing_num.rec_num
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
            inner join ing_num
                on ing_num._id = Recipe.id
            where Pantry.id = (%s)
            group by Recipe.id
            order by (COUNT(Ingredient.id)/ing_num.rec_num) desc;

        '''


        conn.run(delete_view)
        #conn.run(create_view)
        result =  conn.runall(create_view+mega_join, pantry_id)
        recipes = []
        for i in result:
            _id = i[2]
            recipe = Recipe.get_recipe_by_id(conn, _id)
            recipe.percentage = i[3]
            recipes.append(recipe)
        return recipes
