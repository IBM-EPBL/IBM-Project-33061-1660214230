from flask import Flask
from flask import redirect,url_for
app=Flask(__name__)
@app.route("/")
def home():
    return "<h1>welcome to flask<h1>"

@app.route("/course")
def courses():
    return "<h1>welcome to Courses<h1>"

@app.route("/hello")
def hello():
    return "<h1>welcome to debug1<h1>"

@app.route("/<name>")
def name(name):
    return f"hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__=='__main__':
    app.run(debug=True)
