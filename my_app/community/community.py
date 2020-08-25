from flask import Blueprint

community_bp = Blueprint('community', __name__, url_prefix='/community')


@community_bp.route('/')
def index():
    return "This is the community section of the web app"
