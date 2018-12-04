from flask import Flask, request
from flask import render_template
import sqlite3


app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

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
    conn.row_factory = dict_factory

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
    if request.method == 'post':
        #add new data
        offer = {}
        offer['name'] = request.form.get('name')
        offer['category'] = request.form.get('category')
        offer['description'] = request.form.get('description')
        offer['location'] = request.form.get('location')
        offer['giver_id'] = request.form.get('giver_id')
        offer['date'] = request.form.get('date')
        offer['time'] = request.form.get('time')

        #save to db
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute("INSERT INTO offer "
                  "(name, category, description, location, giver_id, date, time) "
                  "VALUES "
                  "('{name}', '{category}', '{description}', '{location}', '{giver_id}', '{date}', '{time}') "
                  "".format(**offer))


        #return to page
        return redirect('/user/%s/' % offer['name'])
        pass
    return render_template("add_user.html")


app.run(port=5000)


