from flask import Blueprint

register_bp = Blueprint('register_bp', __name__, template_folder='templates')

from . import routes