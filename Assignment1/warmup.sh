#!/bin/bash

# --------------------- WARMUP --------------------- 
echo Total Tracks:  $(find . -type f | grep \.ogg | wc -l) 
echo
echo Total Artists: $(ls -1dN */*/* | cut -d / -f 3| sort | uniq | wc -l)
echo 
echo -e Multi Genre Artists: '\n'"$(find -mindepth 3 -maxdepth 3 -printf '%f\n' | sort | uniq -d)"
echo 
echo -e Multi Disk Albums: '\n'"$(find -mindepth 5 -maxdepth 5 -iname "dis??" | cut -d/ -f 5 | sort | uniq -d)"
# --------------------- WARMUP ---------------------

# ---------------- DETAILED REPORT -----------------

# ---------------- DETAILED REPORT -----------------
