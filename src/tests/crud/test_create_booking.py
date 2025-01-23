from http.client import responses

import  allure
import  pytest
import logging # this is use to print the message

from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import payload_create_booking
from src.constant.api_constants import APIconstants
from src.utils.utils import Utils

class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify the crete booking status and Booking ID shouldn't be Null ")
    @allure.description("Creating the booking from the payload and verify that booking id shouldn'tbe null")
    def test_create_booking_positive_tc1(self):
        LOGGER =logging.getLogger(__name__)
        LOGGER.info("Starting the testcase of TestCreateBooking")
        LOGGER.info("Post req started")
        response = post_request(
            url= APIconstants().url_create_booking(),
            auth=None,
            headers=Utils().common_header_json(),
            payload= payload_create_booking(),
            in_json=False
        )
        LOGGER.info("Post req done")
        LOGGER.info("Now verifying")
        verify_http_status_cade(response_data=response, expected_data=200)
        LOGGER.info(response.json())
        LOGGER.info(response.json()["bookingid"])
        verify_json_key_not_null(response.json()["bookingid"])
        verify_json_key_gr_zero(response.json()["bookingid"])

    @pytest.mark.negative
    @allure.title("Verify the crete booking status with invalid payload ")
    @allure.description("Creating the booking id invalid and verify 500 status code")
    def test_create_booking_negative_tc2(self):
        response = post_request(
            url= APIconstants().url_create_booking(),
            auth=None,
            headers=Utils().common_header_json(),
            payload= {},
            in_json=False
        )
        verify_http_status_cade(response_data=response, expected_data=500)



