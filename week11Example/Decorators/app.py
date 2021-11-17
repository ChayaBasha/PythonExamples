from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def welcome_greeting() -> 'html':
    return '''<!doctype html>
                <html lang='en'>
                <head>
                    <title>Entry</title>
                    <link href='/static/greeting.css' type='text/css' rel='stylesheet'>
                </head>
                <body>
                    <header>
                    <h1> Please Enter Your Name </h1>
                    </header>
                    <form method= 'POST' action='/greeting'>
                        <input type = 'text' name="name" placeholder = 'enter your name'>
                        <br>
                        <br>
                        <input type='submit' value='enter'>
                    </form>
                </body>
                </html>'''


@app.route('/greeting', methods=['POST'])
def show_greeting() -> 'html':
    return f'''<!doctype html>
                <html lang='en'>
                <head>
                    <title>Greeting</title>
                    <link href='/static/greeting.css' type='text/css' rel='stylesheet'>
                </head>
                <body>
                    <header>
                    <h1> Welcome {request.form['name']}  </h1>
                    </header>
                  
                </body>
                </html>'''


if __name__ == '__main__':
    app.run()
