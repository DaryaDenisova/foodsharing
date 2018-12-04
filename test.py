from flask import Flask, request
from flask import render_template
import sqlite3


app = Flask(__name__)

@app.route("/")
def offer():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template('register page.html')

@app.route('/search')
def search_for_offer():
    # connecting to DB
    conn = sqlite3.connect('app.db')
    c = conn.cursor() #creating cursor to execute queires
    q = request.args.get('query') #getting query from Web

    #handler logic here
    c.execute("SELECT * FROM offer where name LIKE '{q}'".format(q=q))
    offer = list(c.fetchall())

    #close connection
    conn.close()

    # return resulting html
    return render_template('search.html', offer=offer)

@app.route('/add_user')
def add_user():



app.run(port=5000)


