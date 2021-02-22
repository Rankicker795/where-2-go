from flask import Flask, render_template, redirect, url_for, request
from where_2_go import *

app = Flask(__name__)


@app.route("/success/<location>")
def success(location):
    return f"where-2-go has chosen {location}"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/where_2_go", methods=["POST", "GET"])
def where_2_go():
    if request.method == "POST":
        meal = request.form["meal"]
        dict_ = generate_rest_dict(meal.strip().lower())
        location = make_random_choice(dict_)
        return redirect(url_for("success", location=location))
    else:
        meal = request.args.get("meal")
        dict_ = generate_rest_dict(meal.strip().lower())
        location = make_random_choice(dict_)
        return redirect(url_for("success", location=location))


if __name__ == "__main__":
    app.run(debug=True)
