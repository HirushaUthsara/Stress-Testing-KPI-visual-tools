from flask import Flask, jsonify, request
import random
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/generate', methods=['GET'])
def generate():
    num_points = int(request.args.get('num_points', 100))

    # Generate a sequence with random numbers
    data = [random.randint(0, 100) for _ in range(num_points)]

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
