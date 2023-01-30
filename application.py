from flask import Flask, jsonify
from flask import abort
from flask import make_response
import json

app = Flask(__name__)

students = {
  "tasks": [
    {
      "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
      "done": False,
      "id": 1,
      "title": "Buy groceries"
    },

    {
      "description": "Need to find a good Python tutorial on the web",
      "done": False,
      "id": 2,
      "title": "Learn Python"
    }
  ]
}

@app.route('/students', methods=['GET'])
def get_tasks():
    return jsonify({'students': students})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='localhost', port=9090, debug=True)
