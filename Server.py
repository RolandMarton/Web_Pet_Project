from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/<user>")
def home_page(user=None):
    return render_template("Main.html", user=user)


@app.route("/Internal_link")
def internal_link_flex():
    return render_template("Internal_Link_Flex.html")


@app.route("/Extras")
def advice_giver():
    return render_template("Extras.html")


if __name__ == "__main__":
    app.run(debug=True)
