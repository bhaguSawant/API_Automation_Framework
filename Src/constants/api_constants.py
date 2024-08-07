#APIContaints -Class which contain all the endpoints
# Keep all the URLs

class APIConstants(object):
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

#Update,Put,Patch,Delete -BookingId
    def url_patch_delete(booking_id):
        return "https://restful-booker.herokuapp.com"+str(booking_id)