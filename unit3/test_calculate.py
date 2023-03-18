import unittest
from unit2.calculate import storage, app, add, calculate_year, calculate_month

class TestCalculate(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        storage.update({2020: {5: {2: 15, 3: 11, "summary": 26}, 6: {1: 20, "summary": 20}, "summary": 46}})
        self.app = app.test_client()
    def test_add(self):
        url = "/add"
        self.app.get(url + "/20220720/23")
        self.assertTrue(storage[2022][7][20] == 23)
        self.app.get(url + "/20200520/200")
        self.assertTrue(storage[2020][5][20] == 200)
        self.app.get(url + "/20000830/100")
        self.assertTrue(storage[2000][8][30] == 100)
    def test_calculate_year(self):
        url = "/calculate"
        response_text = self.app.get(url + "/2020").data.decode()
        self.assertTrue(response_text == "46")
        response_text = self.app.get(url + "/2022").data.decode()
        self.assertTrue(response_text == "23")
        response_text = self.app.get(url + "/2000").data.decode()
        self.assertTrue(response_text == "100")
    def test_calculate_month(self):
        url = "/calculate"
        response_text = self.app.get(url + "/2020/05").data.decode()
        self.assertTrue(response_text == "26")
        response_text = self.app.get(url + "/2020/06").data.decode()
        self.assertTrue(response_text == "20")
        response_text = self.app.get(url + "/2022/07").data.decode()
        self.assertTrue(response_text == "23")
    def test_add_error(self):
        self.assertRaises(ValueError, add, "SDSDSADS", 23)
    def test_calculate_zero_storage(self):
        storage.clear()
        url = "/calculate"
        response_text = self.app.get(url + "/2000").data.decode()
        self.assertTrue(response_text == "0")
        response_text = self.app.get(url + "/2020/05").data.decode()
        self.assertTrue(response_text == "0")