"""
  Copyright (c) 2015, Tyler Finethy

  All rights reserved. See LICENSE file for details
"""
# import the unittest class that TestGeosPy will inherit
import unittest
# import the main class
from GeosPy import Geos

class TestGeosPy(unittest.TestCase):
    def setUp(self):
        """setUp creates the class instance of GeosPy"""
        self.geospy = Geos

    def test_fail_init_display_models(self):
        """ensuring error handling on passing a model that doesn't exist"""
        with self.assertRaises(NameError):
            self.geospy("fail")

    def test_should_display_jakartr(self):
        """ensuring Jakartr, the test class is available"""
        self.assertTrue('jakartr' in self.geospy().models)

    def test_set_model_to_jakartr_on_init(self):
        """testing that model can be set on initialization"""
        model = 'jakartr'
        self.geospy = self.geospy(model)
        self.assertTrue(isinstance(self.geospy, Geos))
        self.assertEqual(self.geospy.model, model)

    def test_set_model_to_jakart_on_func_call(self):
        """testing set_model function after initialization"""
        model = 'jakartr'
        self.geospy = self.geospy().set_model(model)
        self.assertTrue(isinstance(self.geospy, Geos))
        self.assertEqual(self.geospy.model, model)

    def test_locate_function(self):
        """testing locate function for jakartr model"""
        user_location_dict = {'1': (0,0), '2': None}
        user_friend_dict = {'1': frozenset([2]), '2': frozenset([None])}
        output = self.geospy('jakartr').locate(user_location_dict, user_friend_dict)
        self.assertEqual(output, {'1': (0,0), '2': (-6.2000, 106.8)})

    def test_jakartr_should_not_have_train_function(self):
        """testing proper error handling"""
        user_location_dict = {'1': (0,0), '2': None}
        user_friend_dict = {'1': frozenset([2]), '2': frozenset([None])}
        with self.assertRaises(AttributeError):
            self.geospy('jakartr').train(user_location_dict, user_friend_dict)
