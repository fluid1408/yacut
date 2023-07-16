from http import HTTPStatus

from flask import jsonify, request

from . import app
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    url_map_obj = URLMap.query.filter_by(short=short_id).first()
    if url_map_obj is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    original_link = url_map_obj.original
    return jsonify({'url': original_link}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def create_short_link():
    data = request.get_json()
    if type(data) != dict:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    url_map = URLMap.from_dict(data)
    url_map.save(data)
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED
