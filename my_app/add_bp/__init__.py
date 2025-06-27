from flask import Blueprint

add_bp = Blueprint('add_bp', __name__, template_folder='templates')

from . import routes