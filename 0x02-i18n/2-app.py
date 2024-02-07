#!/usr/bin/env python3
"""
Flask app with get_locale function using request.accept_languages.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import List

app = Flask(__name__)


class Config:
    """
    Setup babel configuration
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match for the user's preferred language.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Renders the index.html template.
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
