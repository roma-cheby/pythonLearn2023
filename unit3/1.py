import datetime
import unittest

from unit2.hello_world import app

days_test_dict = {0 : "Хорошего понедельника",
                  1 : "Хорошего вторника",
                  2 : "Хорошей среды",
                  3 : "Хорошего четверга",
                  4 : "Хорошей пятницы",
                  5 : "Хорошей субботы",
                  6 : "Хорошего воскресенья"}

class TestMaxNumberApp(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app = app.test_client()
        self.base_url = "/hello-world/"

    def _get_weekday(self):
        current_day = datetime.datetime.today().weekday()
        return days_test_dict[current_day]

    def test_can_get_correct_weekday(self):
        username = "Roma"
        weekday = self._get_weekday()
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)