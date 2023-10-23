from flask import Flask, jsonify, request
from flask_restful import Resource

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "HIII"

@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = request.args.get('age')
    return jsonify(message=f"hi  {name}: {age}")

#api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)