import unittest
from mathlit import add 
from mathlit import subtract
from mathlit import multiply
from mathlit import divide

class TestMathtestCase(unittest.TestCase):

    def test_add(self):
        assert add(2, 2) ==4, "2 plus 2 should equal 4"

    def test_subtract(self):
        assert subtract(5, 3) ==2 "5 minus 3 should equal 2"

    def test_multiply(self):
        assert multiply(5, 10) ==50 "5 multiply by 10 should equal 50"

    def test_divide(self):
        assert divide(15, 3) ==5 "15 divided by 3 should equal 5"

