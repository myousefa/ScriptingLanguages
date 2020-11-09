#! /usr/bin/env bash

# Problem2
#  Find all awk scripts under the current directory and change the #! line from /usr/local/bin/gawk
#  to /usr/bin/gawk



# Get first line 
find . -iname '*.awk' -print |
while read filename; do
    test -n "$(sed -n -e "/#!.*awk/p ; 1q" $filename)" && sed -i '1s|local/||' $filename ; 
done 
# Modify line
