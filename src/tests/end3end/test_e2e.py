from http.client import responses

import allure
import pytest

from src.constant.api_constants import APIconstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils
from confest import create_token,get_booking_id

class TestE2e(object):

    @allure.title("verify E2E create booking -> update booking -> deletebooking")
    @allure.description(" I want verify the crud oper")
    def test_update_booking_with_id_token(self,create_token,get_booking_id):
        booking_id=get_booking_id
        token = create_token
        put_url =APIconstants.url_patch_put_delete(booking_id=booking_id)
        print(put_url)
        response =put_requests(
            url=put_url,
            headers=Utils().common_header_put_patch_delete_cookie(token=token),
            payload=payload_update_booking(),
            auth=None,
            in_json=False)
        print(response)
        verify_http_status_code(response_data=response,expected_data=200)
        verify_response_key(response.json()["firstname"],expected_data="Amit")
        verify_response_key(response.json()["lastname"], expected_data="Brown")



    @allure.title("E2E Delete- booking")
    @allure.description(" Verify booking gets deleted with is and token")
    def test_delete_booking_id(self,create_token,get_booking_id):
        booking_id = get_booking_id
        token = create_token

        delete_url = APIconstants.url_patch_put_delete(booking_id=booking_id)
        print(delete_url)
        response = delete_requests(
            url=delete_url,
            headers=Utils().common_header_put_patch_delete_cookie(token=token),
            auth=None,
            in_json=False
        )
        print(response)
        verify_http_status_code(response_data=response, expected_data=201)
        verify_response_delete(response=response.text)

