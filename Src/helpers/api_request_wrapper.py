import json
import requests

def get_request(url,auth):
    response = requests.get(url=url,auth=auth)
    return  response.json()

def post_request(url,auth,headers,payload,in_json):
    post_response = requests.post(url=url, headers=headers,auth=auth, data= json.dump(post_request()))
    if in_json is True:
        return  post_response()
    return post_response

def patch_request(url,headers,auth,payload, in_json):
    patch_response_data = requests.patch(url=url, headers=headers,auth=auth, data=json.dump(patch_request()))
    if in_json is True:
        return  patch_response_data.json()
    return patch_response_data


def put_request(url,headers,auth,payload, in_json):
    put_response_data = requests.put(url=url, headers=headers,auth=auth, data=json.dump(put_request()))
    if in_json is True:
        return put_response_data.json()
    return put_response_data


def delete_request(url,headers,auth,payload, in_json):
    delete_response_data = requests.delete(url=url, headers=headers,auth=auth, data=json.dump(delete_request()))
    if in_json is True:
        return  delete_response_data.json()
    return delete_response_data



