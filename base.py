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
        pass

class UnsortedList(Base):
    def __init__(self):
        self.data = []

    def insert(self, data):
        for elm in data:
            self.data.append(elm)

    def p(self):
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(', '.join(self.data))

class SortedList(Base):
    def __init(self):
        self.data = []

if __name__ == '__main__':
    initialize_champs()
