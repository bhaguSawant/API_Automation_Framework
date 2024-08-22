#Contains common utilities
#read data from csv file
# read data from excel file
# set header -application/json , application/xml

class Utils(object):
    def common_headers_json(self):
        headers={
            "Content_Type":"application/json"
        }
        return headers

    def common_header_put_patch_delete_basic_auth(self,basic_auth_value):
        headers={
            "Content-Type":"application/json",
            "Authorization":"Basic"+str(basic_auth_value),
        }
        return headers

    def common_header_put_delete_patch_cookie(self, token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "Basic" + str(token),
        }
        return headers

    def common_headers_xml(self):
        headers={
            "Content_Type":"application/xml"
        }
        return headers



    def read_csv_file(self):
        pass

    def read_env_file(self):
        pass

    def read_database(self):
        pass

