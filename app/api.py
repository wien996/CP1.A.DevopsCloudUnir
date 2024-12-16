import http.client

from flask import Flask

from app import util
from app.calc import Calculator

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


@api_application.route('/calc/multiply/<int:num1>/<int:num2>', methods=['GET'])
def multiply(num1, num2):
    try:
        result = num1 * num2
        return jsonify({"operation": "multiply", "result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_application.route('/calc/divide/<int:x>/<int:y>', methods=['GET'])
def divide(x, y):
    try:
        if num2 == 0:
            return jsonify({"error": "Divisor cannot be zero"}), 406
        result = num1 / num2
        return jsonify({"operation": "divide", "result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
