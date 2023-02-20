from flask import jsonify, request, url_for

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import validate_custom_id, get_unique_short_id


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': url_map.original}), 200


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса', status_code=400)
    if 'url' not in data:
        raise InvalidAPIUsage(
            '\"url\" является обязательным полем!', status_code=400
        )
    if 'custom_id' in data and data['custom_id'] not in (None, ''):
        validate_custom_id(data['custom_id'])
        short = data['custom_id']
    else:
        short = get_unique_short_id()
    url_map = URLMap(
        original=data['url'],
        short=short
    )
    db.session.add(url_map)
    db.session.commit()
    return jsonify(
        {
            'url': url_map.original,
            'short_link': url_for('index_view', _external=True) + url_map.short
        }
    ), 201
