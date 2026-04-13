from flask import Flask, request, jsonify
from business import get_data

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Ares BackEnd API!"

@app.route('/api', methods=['GET'])
def api():
    data = get_data()
    data = {"names": data}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
