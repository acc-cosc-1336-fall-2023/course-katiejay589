#tests that die returns a value between 1 and 6

import unittest
from src.homework.j_classes.class_a import Die

class Test_Config(unittest.TestCase):

    def test_get_rolled_value(self):
        die = Die
        die.roll(self)
        self.assertIn(die.get_rolled_value(self), range(1,7))
        die.roll(self)
        self.assertIn(die.get_rolled_value(self), range(1,7))
        die.roll(self)
        self.assertIn(die.get_rolled_value(self), range(1,7))
        

