#!/usr/bin/env python3 

import os 
import project 
import unittest 
from flask_testing import TestCase
from flask import Flask, jsonify
#import base 

class ProjectTestCase(TestCase):
    '''
    Testing Suite for LoLBurst, for use in Travis CI 
    '''
    
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

    # Why the fuck does this not work
    '''
    def test_backend(self):
        resp = self.client.get('/backend')
        self.assertEquals(resp.json, jsonify({"Please":"Work", "Derp": "SOWWY"}))
    '''

    def test_info_html(self):
        rv = self.app.get('/info')
        self.assert_template_used('info.html')

    def test_stats_html(self):
        rv = self.app.get('/stats')
        self.assert_template_used('stats.html')

if __name__ == '__main__': 
    unittest.main()

