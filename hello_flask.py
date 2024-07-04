# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5


# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def hello():
  return render_template('index.html')

# @app.route('/avner')
# def prof():
#   return 'El Jefe'
