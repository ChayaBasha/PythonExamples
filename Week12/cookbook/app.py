from flask import Flask, render_template
import ast

app = Flask(__name__)

recipeDict = {}

readCookBook = open('./cookBook.txt', 'r')
# this reads the file as python code
recipeDict = ast.literal_eval(readCookBook.read())
readCookBook.close()


@app.route('/')
def show_home():
    return render_template("index.html")


@app.route('/recipeCards')
def generate_cards():
    return render_template("recipe4.html", recipeDict = recipeDict)


if __name__ == '__main__':
    app.run()
