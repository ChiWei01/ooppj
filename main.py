from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/routechecker")
def routechecker():
    return render_template("routechecker.html")


@app.route("/caloriescalculator")
def caloriescalculator():
    return render_template("caloriescalculator.html")


@app.route("/farecalculator")
def farecalculator():
    return render_template("farecalculator.html")


@app.route("/repairshop")
def repairshop():
    return render_template("repairshop.html")


@app.route("/socialzone")
def socialzone():
    return render_template("socialzone.html")


@app.route("/customisation")
def customisation():
    return render_template("customisation.html")


@app.route("/happening")
def happening():
    return render_template("happening.html")


if __name__ == "__main__":
    app.run(debug=True)
