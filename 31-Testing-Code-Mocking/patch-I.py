import urllib.request
import unittest
from unittest.mock import patch

class WebRequest():
    def __init__(self, url):
        self.url = url
    
    def execute(self):
        # get a response object back after making a request
        # to open the url
        response = urllib.request.urlopen(self.url)

        if response.status == 200:
            return "SUCCESS"

        return "FAILURE"

# wr = WebRequest("http://www.google.com")
# print(wr.execute())

class WebRequestTest(unittest.TestCase):
    def test_execute_with_success_response(self):
        # patch("package.module.attribute")
        with patch("urllib.request.urlopen") as mock_urlopen:
            # mock_urlopen is an object mocking the
            # request we got back from calling .urlopen()
            # we want that object's return_value's status
            # to be 200 to test if the execute() method
            # returns the right value
            
            wr = WebRequest("http://www.google.com")
            mock_urlopen.return_value.status = 200

            self.assertEqual(wr.execute(), "SUCCESS")
    
    def test_execute_with_failure_response(self):
        with patch("urllib.request.urlopen") as mock_urlopen:
            wr = WebRequest("http://www.google.com")
            mock_urlopen.return_value.status = 404
            
            self.assertEqual(wr.execute(), "FAILURE")

if __name__ == "__main__":
    unittest.main()