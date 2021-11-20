import sqlite3

def db_conect():
    db_name = "cookBook.sqlite"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row

    return conn


con = db_conect()
cur = con.cursor()
cur.execute('DROP TABLE recipeBase;')
readRecipeBase = open('recipeBase.csv', 'r')
lines = readRecipeBase.readlines()
readRecipeBase.close()
headers = lines[0].strip().replace('\'', '').split(',')
values = []
for k, line in enumerate(lines):
    if (k>0):
        k = line.strip().replace('\'',"").split(',')
        values.append(tuple(k))

cur.execute(f'''CREATE TABLE recipeBase({headers[0]} TEXT primary key, {headers[1]} INTEGER );''')
cur.executemany(f'''INSERT INTO recipeBase({headers[0]},{headers[1]}) VALUES(?,?);''', values)

cur.execute('DROP TABLE recipes;')
readfajitasIngredients = open('fajitasIngredients.csv', 'r')
dishName = readfajitasIngredients.name.replace('Ingredients.csv','')
fajitasLines = readfajitasIngredients.readlines()
readfajitasIngredients.close()
fajitasHeaders = fajitasLines[0].strip().replace('\'', '').split(',')
fajitasIngredientValues = []
for k, line in enumerate(fajitasLines):
     if (k>0):
         k = line.strip().replace('\'',"").split(',')
         fajitasIngredientValues.append((dishName,) + tuple(k))

cur.execute(f'''CREATE TABLE recipes(
id INTEGER primary key autoincrement, 
recipe_name TEXT, 
{fajitasHeaders[0]} TEXT, 
{fajitasHeaders[1]} INTEGER, 
{fajitasHeaders[2]} TEXT,
 foreign key ('recipe_name') REFERENCES recipeBase(recipe_name));''')

cur.executemany(f'''INSERT INTO recipes(recipe_name,{fajitasHeaders[0]},{fajitasHeaders[1]}, {fajitasHeaders[2]}) 
VALUES(?,?,?,?);''', fajitasIngredientValues)


readGuacamoleIngredients = open('guacamoleIngredients.csv', 'r')
dishName = readGuacamoleIngredients.name.replace('Ingredients.csv','')
guacamoleLines = readGuacamoleIngredients.readlines()
readGuacamoleIngredients.close()
guacamoleHeaders = guacamoleLines[0].strip().replace('\'', '').split(',')
guacamoleIngredientValues = []
for k, line in enumerate(guacamoleLines):
     if (k>0):
         k = line.strip().replace('\'',"").split(',')
         guacamoleIngredientValues.append((dishName,) + tuple(k))

cur.executemany(f'''INSERT INTO recipes(recipe_name,{guacamoleHeaders[0]},{guacamoleHeaders[1]}, {guacamoleHeaders[2]}) 
VALUES(?,?,?,?);''', guacamoleIngredientValues)

readMargaritasIngredients = open('margaritasIngredients.csv', 'r')
dishName = readMargaritasIngredients.name.replace('Ingredients.csv','')
margaritasLines = readMargaritasIngredients.readlines()
readMargaritasIngredients.close()
margaritasHeaders = margaritasLines[0].strip().replace('\'', '').split(',')
margaritasIngredientValues = []
for k, line in enumerate(margaritasLines):
     if (k>0):
         k = line.strip().replace('\'',"").split(',')
         margaritasIngredientValues.append((dishName,) + tuple(k))

cur.executemany(f'''INSERT INTO recipes(recipe_name,{margaritasHeaders[0]},{margaritasHeaders[1]}, {margaritasHeaders[2]}) 
VALUES(?,?,?,?);''', margaritasIngredientValues)


con.commit()
con.close()