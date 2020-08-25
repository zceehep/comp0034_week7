from flask import Blueprint

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return "This is the home page of the web app"
