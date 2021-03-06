from flask import json
from requests import codes


def request_json(client, method, url, body=None, status=codes.ok):
    request = getattr(client, method)
    response = request(url, data=json.dumps(body),
                       content_type='application/json')
    assert response.status_code == status
    response_body = json.loads(response.get_data(as_text=True))
    return response_body


def create_post(client, body):
    response_body = request_json(client, 'post', '/posts', body, codes.created)
    assert type(response_body['id']) is int

    return response_body
