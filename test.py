from flask import Flask, request, redirect
from flask import render_template
import sqlite3

application = Flask(__name__)
#import app.myviews

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d




@application.route("/")
def offer():
    return render_template('index.html')


@application.route('/register', methods=['GET', 'POST'])
def register():

    user_created = False
    error_message = ""

    if request.method == 'POST':
        #add new data
        users = {}
        users['login'] = request.form.get('login')

        #save to db
        conn = sqlite3.connect('app.db')
        c = conn.cursor()

        c.execute("SELECT * FROM users where login='%s'" % users['login'])
        if c.fetchone():
            # user with this login is already in my database
            error_message = "user_exists"
            return render_template("warning2.html")
        else:
            c.execute("INSERT INTO users "
                      "(login) "
                      "VALUES "
                      "('{login}')"
                      "".format(**users))
            conn.commit()
            user_created = True
        conn.close()
        # redirect to user page
        return redirect('/users/%s/' % users['login'])
    return render_template(
    "register.html",
    user_created=user_created,
    error_message=error_message
    )


@application.route('/users/<login>/')
def user_page(login):
    conn = sqlite3.connect('app.db ')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM users WHERE login='%s'" % login)
    user_data = c.fetchone()

    # Close connection
    conn.close()
    return render_template("userpage.html", user=user_data)



@application.route('/search', methods=['GET', 'POST'])
def search_for_offer():
    if request.method == 'POST':
        query = request.form.get('name')
        conn = sqlite3.connect('app.db')
        conn.row_factory = dict_factory
        c = conn.cursor()
        if query:
            c.execute("SELECT * FROM offer WHERE name LIKE '%{query}%'"
                      "".format(query=query))
            offer_data = list(c.fetchall())
            conn.close()

            if offer_data != []:
         #       return render_template("result.html", offers=offer_data)
                return redirect('/result/%s' % query)
            else:
                return render_template("warning3.html")

        else:
            return render_template("warning3.html")

    return render_template("search.html")


@application.route('/result/<query>')
def search_result(query):
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
 #   if request.method == 'GET':
    c.execute("SELECT * FROM offer WHERE name LIKE '%{query}%'"
                      "".format(query=query))
    offer_data =list(c.fetchall())
    conn.close()
  #  else:
#      if request.form['giver_id']:
#        user = {}
#        user.update({'id': request.form('giver_id')})
#        user['id'] = request.form('giver_id')
#        user_id = request.form('giver_id')
   #     m = {}
  #      m['message'] = request.form.get('message')
 #         user['id'] = request.form.get('giver_id')
 #       c.execute("SELECT * FROM users WHERE user_id='%s'" % user_id)
 #       user_data =c.fetchone()
 #       conn.close()
 #    print(user['id'])
       # us_id = offer_data[3]
 #       return redirect('/connect/%s' % user_id)
     #   return redirect('/connect')
    return render_template("result.html", offers=offer_data)

@application.route('/connect')
def connect():
 #   conn = sqlite3.connect('app.db')
  #  conn.row_factory = dict_factory
   # c = conn.cursor()

  #  user = {}
  #  user['id'] = request.form.get('giver_id')
  #  c.execute("SELECT * FROM users WHERE user_id='%s'" % user["id"])
  #  user_data =c.fetchone()
  #  conn.close()

    return render_template("connect.html")


@application.route('/offer/<offer_id>/')
def offer_page(offer_id):
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM offer WHERE offer_id='%s'" % offer_id)
    offer_data = c.fetchone()
    print(offer_data)
    # Close connection
    conn.close()
    return render_template("offerpage.html", offer=offer_data)



@application.route('/add_offer', methods=['GET', 'POST'])
def add_offer():
    if request.method == 'POST':
        #add new data
        offer = {}
        offer['name'] = request.form.get('name')
        offer['category'] = request.form.get('category')
        offer['description'] = request.form.get('description')
        offer['location'] = request.form.get('location')
        offer['login'] = request.form.get('login')
        offer['date'] = request.form.get('date')
        offer['time'] = request.form.get('time')

        login = request.form.get('login')
        #save to db
        conn = sqlite3.connect('app.db')
        c = conn.cursor()

        c.execute("SELECT user_id FROM users WHERE login='%s'" % offer["login"])
        if c.fetchone():
            offer.update({'giver_id': c.fetchone()})
            c.execute("INSERT INTO offer "
                      "(name, category, description, location, giver_id, date, time) "
                      "VALUES "
                      "('{name}', '{category}', '{description}', '{location}', '{giver_id}', '{date}', '{time}') "
                      "".format(**offer))
            conn.commit()
            c.execute("SELECT last_insert_rowid()")
            offer_id = c.fetchone()
            conn.close()

            #redirect to offer page
            return redirect('/offer/%s/' % offer_id)
        else:
            return render_template("warning.html")

    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM metro_station ORDER BY station_name ASC")
    metro_stations = c.fetchall()
    conn.close()

    return render_template("add_offer.html",  metro_stations=metro_stations)





application.run(port=5000, debug=True)
