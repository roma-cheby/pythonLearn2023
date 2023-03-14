import unittest

from unit2.decrypt import decrypt

class TestDecrypt(unittest.TestCase):
    def test_decrypt_zero(self):
        self.assertTrue(decrypt(".") == "")
        self.assertTrue(decrypt("абра-кадабра.") == "абра-кадабра")

    def test_decrypt_one(self):
        self.assertTrue(decrypt("абраа..-кадабра") == "абра-кадабра")
        self.assertTrue(decrypt("абраа..-.кадабра") == "абра-кадабра")
        self.assertTrue(decrypt("абра--..кадабра") == "абра-кадабра")
        self.assertTrue(decrypt("абрау...-кадабра") == "абра-кадабра")
        self.assertTrue(decrypt("1..2.3") == "23")

    def test_decrypt_more(self):
        self.assertTrue(decrypt("абра........") == "")
        self.assertTrue(decrypt("абр......a.") == "a")
        self.assertTrue(decrypt("1.......................") == "")
