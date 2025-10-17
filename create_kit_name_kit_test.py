
import pytest
from data import kit_bodies
from sender_stand_request import post_new_client_kit

import json

@pytest.fixture(scope="module")
def auth_token():
    # token fijo
    return "48edca05-3479-4d3b-accc-7c4af4729dd2"

# Funciones de assertion
def positive_assert(kit_body, auth_token):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body, auth_token):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

# Tests positivos
def test_kit_name_min_char(auth_token):
    positive_assert(kit_bodies["min_char"], auth_token)

def test_kit_name_max_char(auth_token):
    positive_assert(kit_bodies["max_char"], auth_token)

def test_kit_name_special_characters(auth_token):
    positive_assert(kit_bodies["special_characters"], auth_token)

def test_kit_name_with_spaces(auth_token):
    positive_assert(kit_bodies["with_spaces"], auth_token)

def test_kit_name_numbers(auth_token):
    positive_assert(kit_bodies["numbers"], auth_token)

# Tests negativos
def test_kit_name_empty(auth_token):
    negative_assert_code_400(kit_bodies["empty"], auth_token)

def test_kit_name_too_long(auth_token):
    negative_assert_code_400(kit_bodies["too_long"], auth_token)

def test_kit_name_not_passed(auth_token):
    negative_assert_code_400(kit_bodies["not_passed"], auth_token)

def test_kit_name_wrong_type(auth_token):
    negative_assert_code_400(kit_bodies["wrong_type"], auth_token)