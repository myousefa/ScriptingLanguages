#! /usr/bin/env bash

#Problem2
#  Find all awk scripts under the current directory and change the #! line from /usr/local/bin/gawk
#  to /usr/bin/gawk



# Get first line 
find . -iname '*.awk' -print |
while read filename; do
    sed -e "s/#! *\/usr\/local\/bin\/gawk/#!\/usr\/bin\/gawk/g" $filename 
done 
# Modify line
