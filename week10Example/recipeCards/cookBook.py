# This creates a simple dictionary
ingredientList = {
    'Peppers': '2',
    'Onion' : '1',
    'Oil' : '1Tbs',
    'Cayenne' : '1/4tsp'
}
ingredientList2 = {
    'cheese':'1Lbs',
    'Butter': '1Tbs',
    'Milk': '1/2C',
    'Pasta': 'box'
}

ingredients3 = {
    'Potato':'4',
    'Carrot': '2',
    'Peas':'1/2C',
    'Coconut Milk': 'can',
    'Curry': '!Tbs'
}

ingredinets4 = {
    'avacado': '4',
    'Lime': '1/2',
    'Garlic': 1
}

ingredinets5 = {
    'Tequilla': '2 shots',
    'Lime': '1',
    'Cointreau': '1 shot'
}

# this is our cook Book
cookBook = {}

cookBook['fajitas'] = {
    'Dish Type': 'Main',
    'Prep Time': '20 min',
    'Ingredients': ingredientList
}
cookBook['Coconut Curry'] = {
    'Dish Type': 'Main',
    'Prep Time': '40 min',
    'Ingredients': ingredients3
}

cookBook['Mac N Cheese'] = {
    'Dish Type': 'Main',
    'Prep Time': '20 minutes',
    'Ingredients': ingredientList2
}

cookBook['Guacamole'] = {
    'Dish Type': 'side',
    'Prep Time': '5 min',
    'Ingredients': ingredinets4
}

cookBook['Margaritas'] = {
    'Dish Type': 'drink',
    'Prep Time': '5 min',
    'Ingredients': ingredinets5
}

# #Lets print it to a file
printedCookBook = open('cookBook.txt', 'w')
printedCookBook.write(str(cookBook))
printedCookBook.close()

printedCookBook.close
