from utils import request_builder
import pytest


@pytest.mark.get
def test_get_posts(url):
    response = request_builder.send_request(method='GET', url=url + 'posts', data=None)
    assert response.status_code == 200
    assert response.json()[1]['title'] == 'qui est esse'


@pytest.mark.get
def test_get_comments(url):
    response = request_builder.send_request(method='GET', url=url + 'comments', data=None)
    assert response.status_code == 200
    assert response.json()[0]['email'] == 'Eliseo@gardner.biz'


@pytest.mark.get
def test_get_albums(url):
    response = request_builder.send_request(method='GET', url=url + 'albums', data=None)
    assert response.status_code == 200
    assert response.json()[1]['title'] == 'sunt qui excepturi placeat culpa'


@pytest.mark.get
def test_get_photos(url):
    response = request_builder.send_request(method='GET', url=url + 'photos', data=None)
    assert response.status_code == 200
    assert response.json()[2]['url'] == 'https://via.placeholder.com/600/24f355'


@pytest.mark.get
def test_get_todos(url):
    response = request_builder.send_request(method='GET', url=url + 'todos', data=None)
    assert response.status_code == 200
    assert response.json()[1]['title'] == 'quis ut nam facilis et officia qui'


@pytest.mark.get
def test_get_users(url):
    response = request_builder.send_request(method='GET', url=url + 'users/1', data=None)
    assert response.status_code == 200
    assert response.json()['name'] == 'Leanne Graham'


@pytest.mark.post
def test_post_posts(url, posts):
    response = request_builder.send_request(method='POST', url=url + 'posts', data=posts)
    assert response.status_code == 201


@pytest.mark.post
def test_post_comments(url, comments):
    response = request_builder.send_request(method='POST', url=url + 'comments', data=comments)
    assert response.status_code == 201


@pytest.mark.post
def test_post_albums(url, albums):
    response = request_builder.send_request(method='POST', url=url + 'albums', data=albums)
    assert response.status_code == 201


@pytest.mark.post
def test_post_photos(url, photos):
    response = request_builder.send_request(method='POST', url=url + 'photos', data=photos)
    assert response.status_code == 201


@pytest.mark.post
def test_post_todos(url, todos):
    response = request_builder.send_request(method='POST', url=url + 'todos', data=todos)
    assert response.status_code == 201


@pytest.mark.post
def test_post_users(url, users):
    response = request_builder.send_request(method='POST', url=url + 'users', data=users)
    assert response.status_code == 201


@pytest.mark.put
def test_put_todos(url, todos):
    response = request_builder.send_request(method='PUT', url=url + 'todos/2', data=todos)
    assert response.status_code == 200
    assert response.json() is not None


@pytest.mark.put
def test_put_comments(url, comments):
    response = request_builder.send_request(method='PUT', url=url + 'comments/2', data=comments)
    assert response.status_code == 200
    assert response.json() is not None


@pytest.mark.patch
def test_patch_comments(url, comments):
    response = request_builder.send_request(method='PATCH', url=url + 'comments/3', data=comments)
    assert response.status_code == 200


@pytest.mark.delete
def test_delete_posts(url):
    response = request_builder.send_request(method='DELETE', url=url + 'posts/2', data=None)
    assert response.status_code == 200
    assert response.json() is not None


@pytest.mark.delete
def test_delete_users(url):
    response = request_builder.send_request(method='DELETE', url=url + 'users/5', data=None)
    assert response.status_code == 200


@pytest.mark.negative
def test_invalid_delete_users(url):
    response = request_builder.send_request(method='DELETE', url=url + 'dummy/9999', data=None)
    assert response.status_code == 404
    assert response is not None


@pytest.mark.negative
def test_invalid_post_posts(url, albums):
    response = request_builder.send_request(method='POST', url=url + 'post', data=albums)
    assert response.status_code == 404
    assert response is not None


@pytest.mark.negative
def test_invalid_get_users(url):
    response = request_builder.send_request(method='GET', url=url + 'user', data=None)
    assert response.status_code == 404
    assert response is not None


@pytest.mark.negative
def test_invalid_put_users(url, users):
    response = request_builder.send_request(method='PUT', url=url + 'user/1', data=users)
    assert response.status_code == 404
    assert response.json() is not None


@pytest.mark.negative
def test_invalid_patch_posts(url, posts):
    response = request_builder.send_request(method='PATCH', url=url + 'test/2000', data=posts)
    assert response.status_code == 404
    assert response.json() is not None
