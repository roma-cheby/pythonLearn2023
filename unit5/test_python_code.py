import unittest

from python_code_app import app

class TestRegistrationApp(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = "/python_code"

    def test_timeout_error(self):
        values = {"code" : "import time; time.sleep(10); print(10)", "timeout" : 2}
        request = self.app.post(self.base_url, data = values)
        self.assertIn("Process kill by timeout", request.data.decode())

    def test_invalid_values_code_empty(self):
        values = {"code" : "", "timeout" : 2}
        request = self.app.post(self.base_url, data = values)
        self.assertIn("required", request.data.decode())

    def test_invalid_value_timeout_not_int(self):
        values = {"code": "import time; time.sleep(10); print(10)", "timeout": "ss"}
        request = self.app.post(self.base_url, data = values)
        self.assertIn("integer value", request.data.decode())
        values = {"code": "import time; time.sleep(10); print(10)", "timeout": [2, 4]}
        request = self.app.post(self.base_url, data = values)
        self.assertIn("integer value", request.data.decode())
        values = {"code": "import time; time.sleep(10); print(10)", "timeout": 2.0}
        request = self.app.post(self.base_url, data = values)
        self.assertIn("integer value", request.data.decode())

    def test_invalid_value_timeout_between_1_30(self):
        values = {"code": "import time; time.sleep(10); print(10)", "timeout": 0}
        request = self.app.post(self.base_url, data =values)
        self.assertIn("between 1 and 30", request.data.decode())
        values = {"code": "import time; time.sleep(10); print(10)", "timeout": 31}
        request = self.app.post(self.base_url, data = values)
        self.assertIn("between 1 and 30", request.data.decode())
