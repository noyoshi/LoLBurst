#!/usr/bin/env python3

import json
import pprint

def initialize_champs():
    with open("champion.json") as f:
        champdata = json.load(f)
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
        for elm in data:
            self.data.append(elm)

        self.data.sort()
        # for i, elm in enumerate(data):
        #     if not self.data:
        #         self.data.append(elm)
        #     else:
        #         for j, elm2 in enumerate(self.data):
        #             if elm < elm2:
        #                 break
        #         self.data.insert(j, elm)

class Node():
    def __init__(self):
        self.string = None
        self.children = dict()

    def insert(self, word, index=0):
        curr = word[index]
        if curr not in self.children:
            self.children[curr] = Node()

        if index + 1 == len(word):
            self.children[curr].string = word
        else:
            self.children[curr].insert(word, index+1)

    def get_trie(self, search, index):
        x = []
        for key, value in self.children.items():
            if index >= len(search) or key is search[index]:
                if value.string is not None:
                    x.append(value.string)
                if (value.children != {}):
                    if index + 1 <= len(search):
                        x += value.get_trie(search, index+1)
                    else:
                        x += value.get_trie(search, index)

        return x

class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, data):
        for elm in data:
            self.root.insert(elm)

    def search(self,data, index=0):
        return self.root.get_trie(data, index)

if __name__ == '__main__':
    initialize_champs()
