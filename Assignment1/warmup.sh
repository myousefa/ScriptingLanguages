#!/bin/bash

# --------------------- WARMUP --------------------- 
echo Total Tracks:  $(find . -type f | grep \.ogg | wc -l) 
echo
echo Total Artists: $(ls -1dN */*/* | cut -d / -f 3| sort | uniq | wc -l)
echo 
echo -e Multi Genre Artists: '\n'"$(find -mindepth 3 -maxdepth 3 -printf '%f\n' | sort | uniq -d)"
echo 
echo -e Multi Disk Albums: '\n'"$(find -mindepth 5 -maxdepth 5 -iname "dis??" | cut -d/ -f 5 | sort | uniq -d)"
echo
# --------------------- WARMUP ---------------------

# ---------------- DETAILED REPORT -----------------
echo -e Multi Genre Artists: '\n'"$(find -mindepth 3 -maxdepth 3 -printf '%f\n' | sort | uniq -d)" | while read artists; do
echo "   $artist" find -iname "*$artist*" | cut -d/ -f 2 | sort | uniq | while read genre; do
echo "      $genre"
done 
done
echo
echo -e Multi Disk Albums: '\n'"$(find -mindepth 5 -maxdepth 5 -iname "dis??" | cut -d / -f 5 | sort | uniq -d)"
# ---------------- DETAILED REPORT -----------------