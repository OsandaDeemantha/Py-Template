from flask import Blueprint

from web import util

bp = Blueprint('test', __name__)

@bp.route('/test', methods=['GET'])
def test():
    return 'test'
