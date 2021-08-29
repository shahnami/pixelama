#!/bin/bash
echo "Type in the number of items for the collection [ENTER]:"

read items

echo "Type in the collection name [ENTER]:"

read name

for i in $( eval echo {0..$items} )
do
	python3 draw_llama.py --save $name-$i
done