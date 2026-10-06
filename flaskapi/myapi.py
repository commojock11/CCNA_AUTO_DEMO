from flask import Flask, request, jsonify, Response
from classes.mycar import Car
from functools import wraps


app = Flask(__name__)
@app.route('/api', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, from your Flask API"})

@app.route('/api/car', methods=['POST'])
def handle_car_request():
    data = request.json
    try:
        make = data.get("make")
        model = data.get("model")
        year = data.get("year")

        if not all([make, model, year]):
            return jsonify({"error": "Missing required fields"}), 400
        car = Car(make, model, year)
        return jsonify({'car': car.__dict__}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


###
# Authentication Logic
###
VALID_USERNAME = "admin"
VALID_PASSWORD = "secret"

def check_authentication(username, password):
    return username == VALID_USERNAME and password == VALID_PASSWORD

def authenticate():
    return Response("Could not validate your credentials", 401, {"WWW-Authenticate": "Basic realm=\"Login Required\""})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_authentication(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
@app.route('/protected')
@requires_auth
def protected():
    return jsonify({"message": "You have accessed a protected route"})
###
# Stop Auth logic
###

if __name__ == "__main__":
    app.run(debug=True)