import allure
import pytest

class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("verify that create booking status and booking ID shoudn't be null")
    @allure.description("Creating Booking from the payload and verify that booking id should not be and same")

    def test_create_booking_positive(self):
        pass