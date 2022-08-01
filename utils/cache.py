import arrow
from flask import request, current_app
from flask_caching import Cache
from redis import Redis

cache = Cache()

cache2 = {
    # "/laoshi": {"data": "data", "time": 12345676},
    # "/xueshe": {"data": "data", "time": 12345676},

}


def redis_cil():
    return current_app.extensions["cache"][cache]._read_client


def redis_get(key: str):
    cil = redis_cil()
    return cil.get(key)



def redis_set(key: str, value: str):
    cil: Redis = redis_cil()
    cil.set(key, value)

def redis_has(ket: str, value):
    ...


def my_cache(time_out: int):
    def warp(fun):
        def inner(*args, **kwargs):
            # 请求时间
            new_time = arrow.get().int_timestamp

            # 缓存接口隔离
            url_path = request.path
            if url_path not in cache2:
                cache2[url_path] = {"data": fun(*args, **kwargs),
                                    "time": new_time}

            # 缓存时间处理
            if new_time > cache2[url_path]["time"] + time_out:
                cache2[url_path] = {"data": fun(*args, **kwargs),
                                    "time": new_time}
            return cache2[url_path]["data"]

        return inner

    return warp
