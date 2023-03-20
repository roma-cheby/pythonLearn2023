import unittest

from unit4.phone_validator import app

class TestRegistrationApp(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = "/registration"
        self.valid_args = dict(email="ahidovroman@mail.ru", phone=9526631905,
                               name="Roman", address="Kominterna 5",
                               index=23233, comment="коммент")

    def test_email_valid(self):
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Ok", response.data.decode())
        self.valid_args["email"] = "ahidovroman@mail.com"
        response = self.app.post(self.base_url, data =self.valid_args)
        self.assertIn("Ok", response.data.decode())

    def test_email_invalid(self):
        self.valid_args["email"] = "ahidovroman"
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Ok", response.data.decode())
        self.valid_args["email"] = "ahidovroman@mail"
        response = self.app.post(self.base_url, data =self.valid_args)
        self.assertNotIn("Ok", response.data.decode())

    def test_email_empty(self):
        self.valid_args.pop("email")
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Ok", response.data.decode())

    def test_phone_valid(self):
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Ok", response.data.decode())
        self.valid_args["phone"] = 9523265905
        response = self.app.post(self.base_url, data =self.valid_args)
        self.assertIn("Ok", response.data.decode())

    def test_phone_invalid_length(self):
        self.valid_args["phone"] = 454543
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Ok", response.data.decode())

    def test_phone_invalid_negative(self):
        self.valid_args["phone"] = -952663190
        response = self.app.post(self.base_url, data =self.valid_args)
        self.assertNotIn("Ok", response.data.decode())

    def test_phone_invalid_type(self):
        self.valid_args["phone"] = "sdsdds"
        response = self.app.post(self.base_url, data =self.valid_args)
        self.assertNotIn("Ok", response.data.decode())

    def test_phone_empty(self):
        self.valid_args.pop("phone")
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Ok", response.data.decode())

    def test_name_valid(self):
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Ok", response.data.decode())
        self.valid_args["name"] = "ROMAN"
        response = self.app.post(self.base_url, data =self.valid_args)
        self.assertIn("Ok", response.data.decode())

    def test_name_empty(self):
        self.valid_args.pop("name")
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Ok", response.data.decode())

    def test_address_valid(self):
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Ok", response.data.decode())
        self.valid_args["address"] = 23232
        response = self.app.post(self.base_url, data =self.valid_args)
        self.assertIn("Ok", response.data.decode())

    def test_address_empty(self):
        self.valid_args.pop("address")
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Ok", response.data.decode())

    def test_index_valid(self):
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Ok", response.data.decode())
        self.valid_args["index"] = 23232
        response = self.app.post(self.base_url, data =self.valid_args)
        self.assertIn("Ok", response.data.decode())

    def test_index_invalid_type(self):
        self.valid_args["index"] = "sdsdds"
        response = self.app.post(self.base_url, data =self.valid_args)
        self.assertNotIn("Ok", response.data.decode())

    def test_index_empty(self):
        self.valid_args.pop("index")
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Ok", response.data.decode())

    def test_comment_valid(self):
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Ok", response.data.decode())
        self.valid_args["comment"] = 23232
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Ok", response.data.decode())

    def test_comment_valid_none(self):
        self.valid_args.pop("comment")
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Ok", response.data.decode())