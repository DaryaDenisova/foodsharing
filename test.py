
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def offer():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template('register page.html')

app.run(port=5000)


