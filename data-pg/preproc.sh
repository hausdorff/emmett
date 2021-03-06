#!/bin/bash
# Cats logs together, strips everything not matching the querystring format
# specified by Philip Guo, and puts all that in one file. One line per
# query string.

for file in *.log*
do
	mv "$file" "${file/.log/}.log"
done

cat *.log | grep -e "web_exec_py[23]\(-1\)\?.py" | grep -oP "user_script=.*? " > all.txt
