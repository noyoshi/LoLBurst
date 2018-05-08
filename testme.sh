#!/bin/bash 

use_temp () {
    cat temp_r | head -n2 
    cat temp_r | tail -n1 | cut -f2 -d$'\t'  
    rm temp_r
    echo ""
}

chmod +x test_project.py
echo "Running unit tests"
./test_project.py
rm temp_r &> /dev/null
rm test_d.txt &> /dev/null
chmod +x benchmark.py
make &> /dev/null 
unzip td.zip

echo 'Testing search time'
echo ""
echo 'Testing sorted'
echo ""
echo "=============="
echo "a"
cat test_d.txt | ./measure ./benchmark.py -s "a" > temp_r
use_temp
echo "ka"
cat test_d.txt | ./measure ./benchmark.py -s "ka" > temp_r 
use_temp
echo "z"
cat test_d.txt | ./measure ./benchmark.py -s "z" > temp_r
use_temp
echo "man"
cat test_d.txt | ./measure ./benchmark.py -s "man" > temp_r 
use_temp


echo 'Testing unsorted'
echo "================"
echo "a"
cat test_d.txt | ./measure ./benchmark.py -u "a" > temp_r
use_temp
echo "ka"
cat test_d.txt | ./measure ./benchmark.py -u "ka" > temp_r
use_temp
echo "z"
cat test_d.txt | ./measure ./benchmark.py -u "z" > temp_r
use_temp
echo "man"
cat test_d.txt | ./measure ./benchmark.py -u "man" > temp_r 
use_temp

echo "Testing trie"
echo "============"
echo "a"
cat test_d.txt | ./measure ./benchmark.py -t "a" > temp_r
use_temp
echo "ka"
cat test_d.txt | ./measure ./benchmark.py -t "ka" > temp_r
use_temp
echo "z"
cat test_d.txt | ./measure ./benchmark.py -t "z" > temp_r
use_temp
echo "man"
cat test_d.txt | ./measure ./benchmark.py -t "man" > temp_r 
use_temp

rm test_d.txt
