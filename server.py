from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "swordfish"
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/result", methods=["POST"])
def result():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    err = False
    if len(name) < 1:
        flash("Name should not be empty")
        err = True
    if len(comment) < 1:
        flash("Comment should not be empty")
        err = True
    if len(comment) > 120:
        flash("Comment is too long. No more than 120 characters")
        err = True
    if err:
        return redirect("/")
    return render_template("result.html", name=name, location=location, language=language, comment=comment)

app.run(debug=True)