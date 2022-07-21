from flask import jsonify
from sqlalchemy.engine.row import Row


def ret_route(data):
    if isinstance(data, Row):
        return jsonify(dict(data))
    elif isinstance(data, list):
        return jsonify([dict(i) for i in data])
    else:
        return jsonify(dict(data))



