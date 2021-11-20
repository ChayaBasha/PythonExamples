from flask import Flask, render_template
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
            recipeDict[recipeKey] = {'Prep Time': recipeBase[1], 'Ingredients': ingredientList}

    return render_template('recipe4.html', recipeDict=recipeDict)


if __name__ == '__main__':
    app.run()
