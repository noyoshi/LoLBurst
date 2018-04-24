#!/bin/sh 

chmod +x benchmark.py
make 

echo "\nTesting sorted"
echo "=============="
cat /usr/share/dict/american-english >> temp_f.txt
cat /usr/share/dict/catala >> temp_f.txt
cat /usr/share/dict/danish >> temp_f.txt
echo "a"
cat temp_f.txt | ./measure ./benchmark.py -s "a" | tail -n1
echo ""
echo "ka"
cat temp_f.txt | ./measure ./benchmark.py -s "ka" | tail -n1
echo ""

echo "Testing unsorted"
echo "================"
echo "a"
cat temp_f.txt | ./measure ./benchmark.py -u "a" | tail -n1
echo ""
echo "ka"
cat temp_f.txt | ./measure ./benchmark.py -u "ka" | tail -n1
echo ""

rm temp_f.txt
