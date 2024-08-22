#Status code we have to maintain in common verification

def verify_http_status_code(response_data, expect_data):
    assert response_data.status_code == expect_data, "Failed ER!=AR"


def verify_response_key(key,expected_data):
    assert key == expected_data


def verify_json_key_for_not_null_token(key):
    assert  key !=0,"Failed -key is non empty" +key


def verify_response_key_should_not_be_none(key):
    assert key is not None

def verify_json_key_for_not_null(key):
    assert key !=0,"Failed -key is non empty" +key
    assert key !=0,"Failed -key is greater than Zero"


def verify_response_delete(response):
    assert "Created" in response