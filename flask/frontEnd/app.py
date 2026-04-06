from flask import Flask, render_template, request
from datetime import datetime
import requests

BACKEND_URL = "http://localhost:8000"

app = Flask(__name__)

@app.route("/")
def home():
    day_of_Week = datetime.today().strftime("%A")
    current_time = datetime.now().strftime("%H:%M:%S")

    return render_template("home.html", day_of_Week=day_of_Week, current_time=current_time)

@app.route("/submit", methods=["POST"])
def submit():
    form_data = dict(request.form)
    requests.post(f"{BACKEND_URL}/submit", json=form_data)

    return "Data submitted successfully"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)