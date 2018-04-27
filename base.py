#!/usr/bin/env python3

import json
import pprint
import time

def initialize_champs():
    with open("champion.json") as f:
        champdata = json.load(f)
        champnames = {}
        for thing in champdata["data"].keys():
            champnames[champdata["data"][thing]["name"]] = thing

    return champnames

def initialize_items():
    with open('item.json') as f:
        itemdata = json.load(f)
        itemnames = {}
        for item in itemdata['data']:
            itemnames[itemdata['data'][item]['name']] = item

    return itemnames

class Base:
    def __init__(self):
        self.data = None

    def insert(self, data):
        pass

    def search(self, key):
        start = time.time()
        if (key):
            results = []
            key = key.lower()
            for elm in self.data:
                if elm.lower().startswith(key):
                    results.append(elm)
            end = time.time()
            print("Search: ", end - start)
            return results
        else:
            end = time.time()
            print("Search: ", end - start)
            return []

    def p(self):
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(', '.join(self.data))

class UnsortedList(Base):
    def __init__(self):
        self.data = []

    def insert(self, data):
        start = time.time()
        for elm in data:
            self.data.append(elm)
        end = time.time()
        print("Insert: ", end-start)

class SortedList(Base):
    def __init__(self):
        self.data = []

    def insert(self, data):
        start = time.time()
        for elm in data:
            self.data.append(elm)

        self.data.sort()
        end = time.time()
        print("Insert: ",end-start)
    def search(self, key):
        start = time.time()
        if key:
            results = []
            key = key.lower()
            found = False
            for index, elm in enumerate(self.data):
                if elm.lower().startswith(key.lower()):
                    found = True
                    results.append(elm)
                elif found:
                    end = time.time()
                    print("Search: ", end-start)
                    return results
            end = time.time()
            print("Search: ", end-start)
            return results
        else:
            end = time.time()
            print("Search: ", end-start)
            return []

class Trie(Base):
    def __init__(self):
        self.root = {}

    def insert(self, data):
        start = time.time()
        for elm in data:
            currlist = self.root
            for char in elm:
                if char.lower() in currlist.keys():
                    currlist = currlist[char.lower()]
                else:
                    currlist[char.lower()] = {}
                    currlist = currlist[char.lower()]

            currlist[0] = elm
        end = time.time()
        print("Insert: ",end-start)

    def search(self,data):
        start = time.time()
        currlist = self.root
        for char in data:
            if char.lower() in currlist.keys():
                currlist = currlist[char.lower()]
            else:
                end = time.time()
                print("Search: ", end-start)
                return []
        x = self.print_dictionary(currlist)
        end = time.time()
        print("Search: ", end-start)
        return x

    def print_dictionary(self, currlist):
        x = []
        if 0 in currlist.keys():
            x.append(currlist[0])
        for key in currlist.keys():
            if key != 0:
                x += self.print_dictionary(currlist[key])
        return x

if __name__ == '__main__':
    initialize_champs()
