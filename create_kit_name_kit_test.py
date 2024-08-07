import configuration
import data
import sender_stand_request


def get_kit_body(name):
    kit_body = {"name": name}
    return kit_body

def positive_assert(kit_body):
    response = sender_stand_request.post_products_kits(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_products_kits(kit_body)
    assert response.status_code == 400

#prueba 1
def test_create_kit_name_1_char():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

#prueba 2
def test_create_kit_name_511_chars():
    kit_body = (get_kit_body
        ("Abcdabcdabcdabcdabcdabcdabcdabcda/"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcda/"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcda/"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd/"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab/"
        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd/"
        "abcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc/"
        "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc/"
        "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab/"
        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab/"
        "cdabcdabcdabcdabC"))
    positive_assert(kit_body)

#prueba 3
def test_create_kit_name_0_chars():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

#prueba 4
def test_create_kit_name_512_chars():
    kit_body = (get_kit_body
        ("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc/"
        "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda/"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc/"
        "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd/"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcda/"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab/"
        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc/"
        "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda/"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcD"))
    negative_assert_code_400(kit_body)

def test_create_kit_name_special_chars():
    kit_body = get_kit_body("№%@")
    positive_assert(kit_body)

def test_create_kit_name_spaces():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)

def test_create_kit_name_numbers():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

def test_create_kit_name_missing():
    kit_body = {}
    negative_assert_code_400(kit_body)

def test_create_kit_name_wrong_type():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)
