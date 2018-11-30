from flask import Flask
from flask import render_template
from flask import request
import db

app = Flask(__name__)


@app.route("/")
def offer():
    return render_template('index.html')


@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/profile")
def profile():
    return render_template('result.html')

@app.route("/search")
def search_for():
    q = request.args.get('query')
    users = db.get_users_by_name()



def

app.run(port=5000)
