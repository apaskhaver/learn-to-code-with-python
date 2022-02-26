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

class WebRequestTest(unittest.TestCase):
    @patch("urllib.request.urlopen")
    # mock_urlopen will represent the mock object gotten 
    def test_execute_with_success_response(self, mock_urlopen):
        # patch("package.module.attribute")
        # with patch("urllib.request.urlopen") as mock_urlopen:
  
        wr = WebRequest("http://www.google.com")
        mock_urlopen.return_value.status = 200

        self.assertEqual(wr.execute(), "SUCCESS")
    
    @patch("urllib.request.urlopen")
    def test_execute_with_failure_response(self, mock_urlopen):
        # with patch("urllib.request.urlopen") as mock_urlopen:
            
        wr = WebRequest("http://www.google.com")
        mock_urlopen.return_value.status = 404

        self.assertEqual(wr.execute(), "FAILURE")

if __name__ == "__main__":
    unittest.main()