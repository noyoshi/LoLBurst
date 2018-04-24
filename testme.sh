#!/bin/sh 

test_python() {
    chomd +x test_project.py
    ./test_project.py 
}

test_dict() { 
    chmod +x benchmark.py
    make
    cat /usr/share/dict/american-english \
        | ./measure ./benchmark.py -s | tail -n1 
}

test_python
test_dict
