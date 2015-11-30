from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def default():
    return render_template("index.html", name = "index", title = "WELCOME")

@app.route("/index")
def index():
    return render_template("index.html", name = "index", title = "WELCOME")

@app.route("/yuecai")
def yuecai():
    return render_template("yuecai.html", name = "yuecai", title = "YUECAI")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html", name = "gallery", title = "GALLERY")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html", name = "calendar", title = "CALENDAR")

@app.errorhandler(404)
def pageNotFound(e):
    return redirect(url_for("default"))

if __name__ == '__main__':
    app.run(debug=True)
