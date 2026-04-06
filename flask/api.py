from flask import Flask,request, render_template

from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    
    dt = datetime.today().strftime("%Y-%m-%d")
    return render_template("index.html", dt=dt)

@app.route("/second")
def second():
    return "Hey! this is 2nd page"

@app.route("/third")
def third():
    return "this is 3rd page"

@app.route("/fourth")
def fourth():
    name = request.args.get("name")
    age = request.args.get("age")

    
    # if age > 18:
    #     return "you are adult to visit this page"
    # else:
    #     return "you are not adult to visit this page"

    return f"Hello {name}, you are {age} years old."

if __name__ == "__main__":
    app.run(debug=True)