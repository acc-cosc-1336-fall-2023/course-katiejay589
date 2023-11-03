#test cases for dictionary file

import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory_dictionary = {}
        add_inventory('widget1', 10, inventory_dictionary)
        self.assertEqual(inventory_dictionary, {'widget1':10})
        add_inventory('widget1', 25, inventory_dictionary)
        self.assertEqual(inventory_dictionary, {'widget1':35})
        add_inventory('widget1', -10, inventory_dictionary), {'widget1':25}

    def test_remove_inventory_widget(self):
        inventory_dictionary = {'widget1':20, 'widget2':10}
        remove_inventory_widget('widget1', inventory_dictionary)
        self.assertEqual(inventory_dictionary, {'widget2':10})
        self.assertEqual(len(inventory_dictionary), 1)

    def test_set_intersection(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(baseball.intersection(basketball), set(['Carmen', 'Alicia']))
    
    def test_set_union(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(baseball.union(basketball), set(['Jodi', 'Carmen', 'Aida', 'Alicia', 'Eva', 'Sarah']))

    def test_set_difference_only_baseball(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(baseball.difference(basketball), set(['Jodi', 'Aida']))

    def test_set_difference_only_basketball(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(basketball.difference(baseball), set(['Eva', 'Sarah']))

    def test_symmetric_difference(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(baseball.symmetric_difference(basketball), set(['Jodi', 'Aida', 'Eva', 'Sarah']))
