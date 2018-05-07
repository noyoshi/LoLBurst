# LoLBurst 

[![Build
Status](https://travis-ci.org/noyoshi/LoLBurst.svg?branch=master)](https://travis-ci.org/noyoshi/LoLBurst)

## Benchmarking 
---

`$ chmod +x testme.sh`

`$ ./testme.sh`

Tests against data that we already validated using `grep -E "^PREFIX.*" | sort` 
and stored in output files to determine that each backends works properly. 

Uses `measure` program to determine memory usage. 

Uses Python's `time` module to determine search / insertion time for each
backend. 

## Installing 
---

- `$ pip3 install -r requirements.txt`
- `$ chmod +x testme.sh`
- `$ FLASK_APP=project.py flask run -h [IPADDRESS]`
