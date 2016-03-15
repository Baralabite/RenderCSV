from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    user = {'nickname': "A-A-Ron"}
    return render_template("index.html", title="Lobby", user=user)

@app.route("/render")
def renderer():
    return "CSV Render"

@app.errorhandler(404)
def not_found(error):
    return "You done messed up, A-A-ron!"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')