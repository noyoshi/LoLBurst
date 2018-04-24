#!/usr/bin/env python3 

import os 
import project 
import unittest 
from flask_testing import TestCase
from flask import Flask, jsonify
import base 

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

    def test_init_champs(self): 
        x = base.initialize_champs()
        assert type(x) == type(['hi'])
        
    def test_unsorted(self): 
        obj = base.UnsortedList()

        ans_list = ["k", "za", "a"]
        champ_names = open("champnames.txt", "r")
        champ_list = [x.strip() for x in champ_names.readlines()]
        
        # Insert into object
        obj.insert(champ_list)

        for a in ans_list: 
            with open("tests/"+ a +"_ans.txt", "r") as f: 
                ans = [x.strip() for x in f.readlines()]
                assert ans == sorted(obj.search(a))

        champ_names.close()
    
    def test_sorted(self): 
        obj = base.SortedList()

        ans_list = ["k", "za", "a"]
        champ_names = open("champnames.txt", "r")
        champ_list = [x.strip() for x in champ_names.readlines()]
        
        # Insert into object
        obj.insert(champ_list)

        for a in ans_list: 
            with open("tests/"+ a +"_ans.txt", "r") as f: 
                ans = [x.strip() for x in f.readlines()]
                assert ans == sorted(obj.search(a))

        champ_names.close()
    
    def test_trie(self): 
        obj = base.Trie()

        ans_list = ["k", "za", "a"]
        champ_names = open("champnames.txt", "r")
        champ_list = [x.strip() for x in champ_names.readlines()]
        
        # Insert into object
        obj.insert(champ_list)

        for a in ans_list: 
            with open("tests/"+ a +"_ans.txt", "r") as f: 
                ans = [x.strip() for x in f.readlines()]
                assert ans == sorted(obj.search(a))

        champ_names.close()



if __name__ == '__main__': 
    unittest.main()

