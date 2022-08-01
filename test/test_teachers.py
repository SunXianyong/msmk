import httpx


def test_url_teachers(teacher_id=2):
    ret = httpx.get(f"http://127.0.0.1:5000/teachers?teacher_id={teacher_id}")
    data = ret.json()
    assert data['code'] == 200
    assert data['data'][1]['name']
    assert data['data'][1]['photo']
