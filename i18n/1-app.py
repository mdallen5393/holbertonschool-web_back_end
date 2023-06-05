#!/usr/bin/env python3
"""Simple flask app with index.html template"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """Class which configures available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/')
def index():
    """Route for `/`"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
