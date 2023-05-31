#!/user/bin/env python3
"""Contains definition for a Basic Flask app"""
from auth import Auth
from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)


@app.route('/')
def index():
    """sets up basic route"""
    return jsonify({"message": "Bienvenue"}), 200


AUTH = Auth()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")