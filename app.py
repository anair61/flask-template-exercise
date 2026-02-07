from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("home.html", page_title="Home")

@app.route("/about")
def about():
    return render_template("about.html", page_title="About")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    submitted = False
    name = ""
    email = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        submitted = True

    return render_template("contact.html", page_title="Contact", submitted=submitted, name=name, email=email)
 
if __name__ == "__main__":
    app.run(debug=True)
