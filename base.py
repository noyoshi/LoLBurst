#!/usr/bin/env python3

import json
import pprint

def initialize_champs():
    champdata = json.load(open("champion.json"))
    champnames = [champdata["data"][thing]["name"] for thing in champdata["data"].keys()]
    return champnames
    #itemdata = json.load(open("item.json"))
    #itemnames = [itemdata['data'][item]['name'] for item in itemdata['data']]

class Base:
    def __init__(self):
        self.data = None

    def insert(self, data):
        pass

    def search(self, key):
        if (key):
            results = []
            key = key.lower()
            for elm in self.data:
                if elm.lower().startswith(key):
                    results.append(elm)

            return results
        else:
            return []

    def p(self):
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(', '.join(self.data))

class UnsortedList(Base):
    def __init__(self):
        self.data = []

    def insert(self, data):
        for elm in data:
            self.data.append(elm)

class SortedList(Base):
    def __init__(self):
        self.data = []

    def insert(self, data):
        for i, elm in enumerate(data):
            if not self.data:
                self.data.append(elm)
            else:
                for j, elm2 in enumerate(self.data):
                    if elm < elm2:
                        break
                self.data.insert(j, elm)
class Node():
    def __init__(self):
        self.word = None
        self.children = dict()

    def addChild(self,word):
        pass

class Trie(Base):
    def __init__(self):
        self.root = Node()

    def insert(self, data):
        for elm in data:
            curr = self.root


    def search(self,data):
        pass

if __name__ == '__main__':
    initialize_champs()
