import unittest
from greeting import greet

class TestGreeting(unittest.TestCase):
    def test_greet(self):
        self.assertEqual("Hi, John", greet("John"))


