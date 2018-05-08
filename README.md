# LoLBurst 

[![Build
Status](https://travis-ci.org/noyoshi/LoLBurst.svg?branch=master)](https://travis-ci.org/noyoshi/LoLBurst)

## Benchmarking 

- `$ chmod +x testme.sh`
- `$ ./testme.sh`

Tests against data that we already validated using `grep -E "^PREFIX.*" | sort` 
and stored in output files to determine that each backend works properly. 

Uses `measure` program to determine memory usage. 

Uses Python's `time` module to determine search / insertion time for each
backend. 

## Installing 

Dependencies: Python 3, pip, Bash, gcc

- `$ git clone https://github.com/noyoshi/LoLBurst`
- `$ cd LoLBurst`
- `$ chmod +x download.sh`
- `$ ./download.sh`
- This will install all requirements for python, and dowload the necessary asset 
files from the API

### Running the server

- `$ FLASK_APP=project.py flask run -h [IPADDRESS]`

### Using back ends for prefix search

- `$ chmod +x benchmark.py`
- `$ cat INPUT_FILE | ./benchmark.py -[ust] "PREFIX"`

### Contribution Breakdown 

##### Timothy Blazek

- Initial front end development
- Created many of the api calling functions 
- Created the prefix tree


##### Edward Atkinson 

- Implemented the sorted and unsorted backends
- Created the javascript used to perform autocompletion on the front end 
- Used javascript to send data to flask backend 


##### Noah Yoshida

- Created tests and integrated them with Travis CI 
- Uploaded code to remote server 
- Created benchmarking functions and gathered data for them 
- Created final demo video and presentation
