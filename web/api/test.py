import requests
from flask import Blueprint, request, jsonify, json

from web import util

bp = Blueprint('test', __name__)
callback_url = f'{util.HOST_URL}/test'

@bp.route('/test', methods=['GET'])
def test():
    return 'test'
