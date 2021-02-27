from flask import Flask, jsonify, request
import pickle
import numpy as np

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run(port=9000, debug=True)
