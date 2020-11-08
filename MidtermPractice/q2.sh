#! /usr/bin/env bash

# Problem2
#  Find all awk scripts under the current directory and change the #! line from /usr/local/bin/gawk
#  to /usr/bin/gawk



# Get first line 
find . -type f | grep \.awk
# Modify line

