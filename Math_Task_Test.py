import unittest
from Math_Task import *

class Math_Task_TestCase(unittest.TestCase):
    def test_maxi_num(self):
        assert maxi_num([5 ,89, 19, 1, 35, 72, 11, 81, 10, 0, 43]) == 89 ,"The max number is 89"

    def test_decend_sorted(self):
        assert decend_sorted([8, 50, 11, 72, 9, 3, 52, 32, 21]) == [72, 52, 50, 32, 21, 11, 9, 8, 3] ,"Decending order"

#****************************************************************************************************


