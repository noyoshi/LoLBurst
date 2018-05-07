# LoLBurst 

[![Build
Status](https://travis-ci.org/noyoshi/LoLBurst.svg?branch=master)](https://travis-ci.org/noyoshi/LoLBurst)

## Benchmarking 

`$ chmod +x testme.sh`

`$ ./testme.sh`

Tests against data that we already validated using `grep -E "^PREFIX.*" | sort` 
and stored in output files to determine that each backends works properly. 

Uses `measure` program to determine memory usage. 

Uses Python's `time` module to determine search / insertion time for each
backend. 

## Installing 

Dependencies: Python 3, pip

- `$ pip3 install -r requirements.txt`
- `$ chmod +x download.py`
- `$ ./download.py`
- `$ chmod +x testme.sh`

### Running the server

- `$ FLASK_APP=project.py flask run -h [IPADDRESS]`

### Using backends for prefix search

- `$ chmod +x benchmark.py`
- `$ cat INPUT_FILE | ./benchmark.py -[ust] "PREFIX"`
