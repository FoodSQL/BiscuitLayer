from connection_helper import ConnectionHelper
from numpy import random

conn = ConnectionHelper()

query = "INSERT INTO Recipe(_name, description, difficulty) VALUES (%s, %s, %s)"
ins_query = "INSERT INTO Recipe_Ingredient(id_recipe, id_ingredient) VALUES (%s, %s)"
del_query = "DELETE FROM Recipe"
del_query2 = "DELETE FROM Recipe_Ingredient"
sel_query = "SELECT * FROM Ingredient"
id_query = "SELECT id FROM Recipe"

conn.run(del_query2)
conn.run(del_query)
ingredients = conn.runall(sel_query)
ingredient_ids = []
for i in ingredients:
    ingredient_ids.append(i[0])


with open("recipes.txt") as json:
    for i in json:
        if (len(i) > 4):
            try:
                conn.run(query, (i, i, random.randint(100)))
            except:
                pass
            # print (i)

recipe_ids = conn.runall(id_query)
for i in recipe_ids:
    random.shuffle(ingredient_ids)
    for j in range(random.randint(7)):
        conn.run(ins_query, (i, ingredient_ids[j]))
