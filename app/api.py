import http.client

from flask import Flask

from app import util
from app.calc import Calculator

from flask import Flask, jsonify, abort

app = Flask(__name__)

CALCULATOR = Calculator()
api_application = Flask(__name__)
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}


@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"


@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.add(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def substract(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.substract(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@app.route('/calc/multiply/<int:x>/<int:y>', methods=['GET'])
def multiply(x, y):
    return jsonify(x * y)

@app.route('/calc/divide/<int:x>/<int:y>', methods=['GET'])
def divide(x, y):
    if y == 0:
        abort(406, description="Divisor cannot be zero")
    return jsonify(x / y)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
