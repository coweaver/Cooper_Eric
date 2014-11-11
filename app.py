from getpage import *
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
	if request.method == "GET":
		return render_template("home.html")
	else:
		team = request.form["team"]
		d = getInfo(team)
		data = getTop(d)
		return render_template("teamPage.html", data=data, team = team)



if __name__ == "__main__":
    app.debug=True
    app.run()
