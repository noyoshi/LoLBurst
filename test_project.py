#!/usr/bin/env python3 

import os 
import project 
import unittest 
from flask_testing import TestCase
from flask import Flask

class ProjectTestCase(TestCase):

    def create_app(self): 
        app = Flask(__name__)
        app.config['TESTING'] = True 
        return app 

    def setUp(self): 
        project.app.testing = True
        self.app = project.app.test_client()

    def test_index(self): 
        rv = self.app.get('/')
        self.assert_template_used('item.html')



if __name__ == '__main__': 
    unittest.main()

