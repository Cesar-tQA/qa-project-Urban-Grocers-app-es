import configuration
import data

def post_new_user(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=data.headers)
    if response.status_code == 201:
        auth_token = response.json().get("authToken")
        return auth_token
    else:
        return None


def post_products_kits(products_ids):
    auth_token = post_new_user(data.user_body)
    if auth_token:
        headers_with_token = data.headers.copy()
        headers_with_token["Authorization"] = f"Bearer {auth_token}"
        response = requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_ids,headers=headers_with_token)
        return response
