from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import pymongo
load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")
client = pymongo.MongoClient(MONGO_URL)
db = client.test
collection = db.test_collection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("page.html")

@app.route("/submit", methods=["POST"])
def submit():
    form_data = dict(request.form)
    collection.insert_one(form_data)

    for item in collection.find():
        print(item)
        del item["_id"]
    return "Data submitted successfully"

if __name__ == "__main__":
    app.run(debug=True)

