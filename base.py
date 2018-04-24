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

    def search(self, key):
        if key:
            results = []
            key = key.lower()
            found = False
            for elm in self.data:
                if elm.lower().startswith(key):
                    found = True
                    results.append(elm)
                elif found:
                    return results
            return results
        else:
            return []

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
        # Gets the current letter of the word wanting to be added
        curr = word[index]
        # checks if that letter is already a child
        if curr not in self.children:
            self.children[curr] = Node()

        if index + 1 == len(word):
            #if last letter in the word, then update the string value of the Node class
            self.children[curr].string = word
        else:
            #if not the last letter, you want to insert the rest of the word to the tree
            self.children[curr].insert(word, index+1)

    def get_trie(self, search, index):
        x = [] #initialize empty list
        for key, value in self.children.items(): #goes through all the children
        #checks to see if on the right level of the Trie or if the key is the same as the current letter
            if index >= len(search) or key.lower() == search[index].lower():
                if value.string and value.string.startswith(search): #Adds the word to the list
                    x.append(value.string)
                if bool(value.children): #if there are children
                    if index < len(search):
                        x += value.get_trie(search, index + 1)
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
