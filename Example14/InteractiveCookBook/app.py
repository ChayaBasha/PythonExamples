from pprint import pprint

from flask import Flask, render_template, request
import sqlite3
import ast

app = Flask(__name__)


def db_conect():
    db_name = "cookBook.sqlite"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row

    return conn


@app.route('/')
def show_home():
    return render_template("index.html")


@app.route('/addRecipe')
def add_Recipe():
    return render_template("addRecipe.html")


@app.route('/recipeAdded', methods=['POST'] )
def recipeAdded():
    recipe_name = request.form['recipe_name']
    dishType = request.form['DishType']
    prepTime = request.form['prepTime']
    ingredients = [(recipe_name,) + others for others in zip(
        request.form.getlist('ingredient_name'),
        request.form.getlist('amount'),
        request.form.getlist('unit')
    )]

    with db_conect() as db:
        cur= db.cursor()
        cur.execute(f'''
        INSERT INTO recipeBase(recipe_name,dish,prep_time) VALUES(?,?,?); ''', (recipe_name, dishType, prepTime))
        pprint(ingredients)
        cur.executemany((f'''
        INSERT INTO recipes(recipe_name,ingredient_name,amount,unit) VALUES(?,?,?,?)'''), ingredients)

    return render_template("recipeAdded.html")


@app.route('/recipeCards')
def generate_cards():
    with db_conect() as db:
        cur = db.cursor()
        cur.execute('''
        SELECT * FROM recipeBase''')
        recipeBases = cur.fetchall()
        recipeDict = {}

        for recipeBase in recipeBases:
            recipeKey = recipeBase[0]

            cur.execute(f'''
                    SELECT recipes.recipe_name, ingredient_name, amount, unit FROM recipes 
                    INNER JOIN recipeBase ON recipes.recipe_name = recipeBase.recipe_name
                    WHERE recipes.recipe_name = '{recipeKey}';''')
            ingredientList = cur.fetchall()
            recipeDict[recipeKey] = {'Dish Type': recipeBase[1],'Prep Time': recipeBase[2], 'Ingredients': ingredientList}

    return render_template('recipe4.html', recipeDict=recipeDict)


if __name__ == '__main__':
    app.run()
