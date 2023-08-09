import json
import pytest


@pytest.fixture
def url():
    return 'https://jsonplaceholder.typicode.com/'


@pytest.fixture
def posts():
    return json.dumps({'title': 'Lorem Ipsum', 'body': 'Lorem Ipsum'})


@pytest.fixture
def comments():
    return json.dumps({'name': 'Lorem Ipsum', 'email': 'user123', 'body': 'Lorem Ipsum'})


@pytest.fixture
def albums():
    return json.dumps({'title': 'Lorem Ipsum'})


@pytest.fixture
def photos():
    return json.dumps({'albumId': 2, 'title': 'Lorem, Lorem, Lorem', 'url': 'https://dummyimage.com/600x400/000/fff&text=hi'})


@pytest.fixture
def todos():
    return json.dumps({'userId': 2, 'title': 'Lorem, ipsum', 'completed': 'false'})


@pytest.fixture
def users():
    return json.dumps({
        'id': 1,
        'name': 'Leanne Graham',
        'username': 'Bret',
        'email': 'Sincere@april.biz',
        'address': {
            'street': 'Kulas Light',
            'suite': 'Apt. 556',
            'city': 'Gwenborough',
            'zipcode': '92998-3874',
            'geo': {
                'lat': '-37.3159',
                'lng': '81.1496'
            }
        },
        'phone': '1-770-736-8031 x56442',
        'website': 'hildegard.org',
        'company': {
            'name': 'Romaguera-Crona',
            'catchPhrase': 'Multi-layered client-server neural-net',
            'bs': 'harness real-time e-markets'
        }
    })
