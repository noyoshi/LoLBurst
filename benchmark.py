#!/usr/bin/env python3 

import sys 
from base import * 

def bench(obj, key):
    s_in = [x.strip() for x in sys.stdin] 
    
    obj.insert(s_in)

    for x in obj.search(key): 
        print(x)

def usage(status): 
    print("Usage: cat DATA_FILE | ./benchmark.py -[ust] KEY") 
    exit(status)

if __name__ == '__main__': 
    if len(sys.argv) > 3:
        usage(0)

    if sys.argv[1] == '-u': 
        obj = UnsortedList() 
    elif sys.argv[1] == '-s': 
        obj = SortedList()
    elif sys.argv[1] == '-t': 
        obj = Trie() 
    else: 
        usage(1)

    key = sys.argv[2]

    bench(obj, key)

