#!/bin/bash 

use_temp () {
    cat temp_r | head -n2 
    cat temp_r | tail -n1 | cut -f2 -d$'\t'  
    rm temp_r
    echo ""
}


chmod +x benchmark.py
make 

echo 'Testing search time'
echo ""
echo 'Testing sorted'
echo ""
echo "=============="
cat /usr/share/dict/american-english >> temp_f.txt
cat /usr/share/dict/catala >> temp_f.txt
cat /usr/share/dict/danish >> temp_f.txt
echo "a"
cat temp_f.txt | ./measure ./benchmark.py -s "a" > temp_r
use_temp
echo "ka"
cat temp_f.txt | ./measure ./benchmark.py -s "ka" > temp_r 
use_temp

echo 'Testing unsorted'
echo "================"
echo "a"
cat temp_f.txt | ./measure ./benchmark.py -u "a" > temp_r
use_temp
echo "ka"
cat temp_f.txt | ./measure ./benchmark.py -u "ka" > temp_r
use_temp

echo "Testing trie"
echo "============"
echo "a"
cat temp_f.txt | ./measure ./benchmark.py -t "a" > temp_r
use_temp
echo "ka"
cat temp_f.txt | ./measure ./benchmark.py -t "ka" > temp_r
use_temp

rm temp_f.txt
