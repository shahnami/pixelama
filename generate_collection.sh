#!/bin/bash

echo "Type in the class type [ENTER]:"

read class_type

echo "Type in the configuration file [ENTER]:"

read config_file

echo "Type in the number of items for the collection [ENTER]:"

read items

echo "Type in the collection name [ENTER]:"

read name

for i in $( eval echo {1..$items} )
do
	python3 main.py --type class_type --config config_file --save $name-$i
done