import requests


def send_request(method, url,  data):
    headers = {'Connection': 'keep-alive',
               'Accept-Encoding': 'gzip, deflate, br'}
    if method == 'GET':
        return requests.get(url=url)
    elif method == 'DELETE':
        return requests.delete(url=url)
    elif method == 'POST':
        return requests.post(url=url, headers=headers, data=data)
    elif method == 'PUT':
        return requests.put(url=url, headers=headers, data=data)
    elif method == 'PATCH':
        return requests.patch(url=url, headers=headers, data=data)