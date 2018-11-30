
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/main")
def offer():
    return render_template('main_map.html')

@app.route("/register")
def register():
    return render_template('register page.html')

@app.route('/search')
def search_for_person():
    q = request.args.get('query')
    users = db.get_users_by_name(q)
    return render_template('search_results.html', q=q, users=users)

app.run(port=5000)


