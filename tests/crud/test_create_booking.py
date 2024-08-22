import allure
import pytest

from Src.helpers.api_request_wrapper import post_request
from Src.constants.api_constants import APIConstants
from Src.helpers.payload_manager import payload_create_booking
from Src.helpers.common_verification import *
from Src.utils.utils import Utils
class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("verify that create booking status and booking ID shoudn't be null")
    @allure.description("Creating Booking from the payload and verify that booking id should not be and same")

    def test_create_booking_positive(self):
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils.common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
             )
        verify_http_status_code(response_data=response,expect_data=200)
        verify_json_key_for_not_null(response.json())["bookingid"]
