import unittest
import datetime
from unit3.person import Person


class TestPerson(unittest.TestCase):
    def test_create_valid(self):
        person1 = Person("Roman", 2003, "Selskaya")
        person2 = Person("Roman", 2003)
    def test_get_age(self):
        person = Person("Roman", 2003, "Selskaya")
        self.assertTrue(person.get_age() == datetime.datetime.now().year - 2003)
    def test_get_name(self):
        person = Person("Roman", 2003, "Selskaya")
        self.assertTrue(person.get_name() == "Roman")
    def test_set_name(self):
        person = Person("Roman", 2003, "Selskaya")
        person.set_name("Artem")
        self.assertTrue(person.get_name() == "Artem")
    def test_get_adress(self):
        person = Person("Roman", 2003, "Selskaya")
        self.assertTrue(person.get_address() == "Selskaya")
    def test_set_adress(self):
        person = Person("Roman", 2003, "Selskaya")
        person.set_address("Kominterna")
        self.assertTrue(person.get_address() == "Kominterna")
    def test_is_homeless(self):
        person = Person("Roman", 2003, "Selskaya")
        self.assertTrue(person.is_homeless() == False)
        person_homeless = Person("Roman", 2003)
        self.assertTrue(person_homeless.is_homeless())