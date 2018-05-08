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

## Overview 

- `project.py` is the flask application used to manage the server and handle
recieving and sending data to and from the front end
- `base.py` contains the backend implementatins for the auto complete / prefix
  searching
- `download.py` and `download.sh` are used to download assets from the Riot Games API and League of
Legends asset API
- `helpers.py` and `item_helper.py` handle API calls and create, manage, and
  parse JSON files (where we store and cache data)
- `measure.c` is the provided measure program to determine memory usage 
- `benchmark.py` is a script to run the backends independently and check for
  time and accuracy 
- `test_project.py` uses the unit testing libraries for Python and Flask to
  create and check accuracy of function calls within the `project.py` file 
- `testme.sh` is the script we run to test the program 
- `tests/` is the folder that contains the outputs for various tests done in
  `test_project.py`
- `templates/` is the folder for flask containing the HTML templates 
- `static/` contain static files for the front end, such as javascript and css
  files, and any downloaded image files 
- `*.json` are all json files containing Riot API static data (cached locally as
  we are limited to 10 calls per hour for this data)


## Contribution Breakdown 

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
