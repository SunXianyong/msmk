from models.model import db


def commit(f):
    def inner(*args, **kwargs):
        ret = f(*args, **kwargs)

        if kwargs.get("commit"):
            db.session.commit()
        return ret

    return inner


@commit
def db_query(commit=None):
    return db.session.query
