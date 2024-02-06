#!/usr/bin/env python3
"""
Flask app with user login emulation, internationalization,
and preferred locale support.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


def get_user(user_id):
    """
    Returns a user dictionary based on user_id.
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Executed before all other functions to find and set the user if any.
    """
    login_as = request.args.get('login_as')
    if login_as:
        user = get_user(int(login_as))
        g.user = user if user else None


@babel.localeselector
def get_locale():
    """
    Determines the best match for the user's preferred language.
    """
    if 'locale' in request.args and \
            request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    if g.user and 'locale' in g.user and \
            g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Renders the 6-index.html template with appropriate message
    based on user's preferred locale.
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
