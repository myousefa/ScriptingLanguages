#!/bin/bash

# --------------------- WARMUP --------------------- 
# Counts total song by ensuring file type is .ogg
echo Total Tracks:  $(find . -type f | grep \.ogg | wc -l) 
echo
# Counts artists by looking into the third part of list of file path and counting it
echo Total Artists: $(ls -1dN */*/*/* | cut -d / -f 3| sort | uniq | wc -l)
echo 
# Finds all multi genre artists by checking in depth 3 and sort and checking for uniqueness
echo -e Multi Genre Artists: '\n'"$(find -mindepth 3 -maxdepth 3 -printf '%f\n' | sort | uniq -d)"
echo 
# Locates a file that is either called disc or disk 5 files deep. If so add path and cut list
echo -e Multi Disk Albums: '\n'"$(find -mindepth 5 -maxdepth 5 -iname "dis??" | cut -d/ -f 5 | sort | uniq -d)"
echo
# --------------------- WARMUP ---------------------

