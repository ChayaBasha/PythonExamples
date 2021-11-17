
# initializing variables
import pprint
import ast
recipeList = []
recipeDict = {}

readCookBook = open('cookBook.txt')
# this reads the file as python code
recipeDict = ast.literal_eval(readCookBook.read())
readCookBook.close()

#creating our new html files and setting them to save in our website
recipeCards = open('../../week10Example/WebstormCode/recipeCards4gen.html', 'w')

# I am going to end up construcing the full html page by creating each piece of it
htmlStart = """<!doctype html>
<html lang = "en">
<head>
    <title>Recipe Card Template</title>
    <link href="css/recipe4.css" type="text/css" rel="stylesheet">
</head>

<body> """

htmlEnd = """
</body>
</html>"""

allHtml = htmlStart
for index, key in enumerate(recipeDict.keys()):
    recipe = recipeDict[key]
    page, cellOnPage = divmod(index, 4)
    row, col = divmod(cellOnPage, 2)
    if row > 1:
        break
    newBlock = f"""
            <div class="cardSize cardColumn{col+1}">
                <p class="fs22">{key}</p>
                <p class="fs12Green">{'Dish Type:' + recipe['Dish Type']}</p>
                <p class="fs12">{'Prep Time:'+ recipe['Prep Time']}</p>
                <span> Ingredients: </span>
                <p class="fs12">{recipe['Ingredients']}</p>
            </div>"""
    if col == 0:
        newBlock = f"""
        <div class="cardRow{row+1}">""" + newBlock
    else:
        newBlock = newBlock + """
        </div>"""

    if cellOnPage == 0:
        newBlock = """<div class="pageSize">""" + newBlock
    elif cellOnPage == 3:
        newBlock += "</div>"

    allHtml += newBlock

if col == 0:
    allHtml += "</div>"

if cellOnPage != 3:
    allHtml += "</div>"

allHtml += htmlEnd

recipeCards.write(allHtml)
recipeCards.close()



