"""Some utilities for the main app.
"""

from functools import wraps
from flask import jsonify


# json endpoint decorator
def json(func):
    """Returning a object gets JSONified. Second part of tuple is the HTML resonse code"""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        return jsonify(func(*args, **kwargs)[0]), func(*args, **kwargs)[1]
    return decorated_function
