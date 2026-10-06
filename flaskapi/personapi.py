from flask import Flask, request, jsonify, Response
from person import Person 
from functools import wraps

app = Flask(__name__)

@app.route('/person', methods=['POST'])
def handle_person_request():
    data = request.json
    try:
        name = data.get('name')
        age = data.get('age')

        if not all ([name, age]):
            return jsonify({"error": "Missing required fields"}), 400

        person = Person(name, age)
        return jsonify({"person": person.__dict__}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)