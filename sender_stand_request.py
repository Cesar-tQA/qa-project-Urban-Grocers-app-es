import configuration
import data



def post_new_user(body, requests=None):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=data.headers)
    if response.status_code == 201:
        auth_token = response.json().get("authToken")
        return auth_token
    else:
        return None
auth_token = post_new_user(data.user_body)


def post_products_kits(products_ids, token, requests=None):
    headers_with_token = data.headers.copy()
    headers_with_token["Authorization"] = f"Bearer {token}"
    response = requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_ids,headers=headers_with_token)
    return response
response = post_products_kits(data.product_ids,auth_token)
print(response.status_code)
print(response.json())