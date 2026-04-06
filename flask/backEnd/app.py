from flask import Flask, request

from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = pymongo.MongoClient(MONGO_URL)

db = client.test

collection = db.test_collection

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    form_data = dict(request.json)
    
    collection.insert_one(form_data)

    return "Data submitted successfully"

@app.route("/view")
def view():
    data = collection.find()   # its a cursor object, we need to convert it into list to access the data
    list_data = list(data)     # converting the cursor object into list to access the data

    for item in list_data:     # iterating through the list of data and deleting the _id field from each item as it is not needed in the output(_id)
        print(item)
        del item["_id"]

    data ={                     # creating a dictionary as the output to return the data in a structured format
        "data": list_data 
    }
    return data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)