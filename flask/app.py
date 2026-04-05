from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, world this is my first flask app and i am learning Flask</p>"

@app.route("/second")
def second():
    return "Hey! this is 2nd page"

@app.route("/third")
def third():
    return "this is 3rd page"

if __name__ == "__main__":
    app.run(debug=True)