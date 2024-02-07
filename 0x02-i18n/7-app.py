#!/usr/bin/env python3
"""
Flask app with user login emulation, internationalization,
preferred locale, and timezone support.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

import pytz

app = Flask(__name__)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    setup babel configuration
    """
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


@babel.timezoneselector
def get_timezone():
    """
    Determines the best match for the user's preferred timezone.
    """
    if 'timezone' in request.args:
        try:
            pytz.timezone(request.args['timezone'])
            return request.args['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user and 'timezone' in g.user:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return 'UTC'


@app.route('/')
def index():
    """
    Renders the 7-index.html template with appropriate message based
    on user's preferred locale and timezone.
    """
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
