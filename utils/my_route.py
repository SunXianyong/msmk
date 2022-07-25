from flask import jsonify
from sqlalchemy.engine.row import Row

from models.model import db
from settings.setting import RESPONSE_CODE


def route_code(data, code=200):
    return jsonify({
        "code": code,
        "msg": RESPONSE_CODE.get(code, "未定义状态"),
        "data": query2dict(data)
    })


def query2dict(data, **kwargs):
    if isinstance(data, Row):
        data = dict(data)
    elif isinstance(data, list):
        data = [dict(i) for i in data]

    for k, v in kwargs.items():
        data[k] = v
    return data


def commit_route(data, code=200):
    db.session.commit()
    return route_code(data, code=code)
