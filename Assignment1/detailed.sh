#!/bin/bash

# ---------------- DETAILED REPORT -----------------
echo -e "Multi Genre Artists: " 
find -mindepth 3 -maxdepth 3 -printf '%f\n' | sort | uniq -d | 
while read artists; do 
    echo "  $artists"
    find -iname "*$artists*" | cut -d/ -f 3 | sort | uniq | 
    while read genres; do
        echo "      $genres"
    done
done
echo

echo -e "Multi Disk Albums: "
find -mindepth 5 -maxdepth 5 -iname "dis??" | cut -d / -f 4 | sort | uniq -d |
while read artists; do
    echo "  $artists"
    find -mindepth 5 -maxdepth 5 -iname "dis??" | grep "$artists" | cut -d / -f 5 | sort | uniq |
    while read albums; do
        echo "       $albums"
    done
done
echo

echo -e "Possible Duplicate Albums: "
find 


exit
    
# ---------------- DETAILED REPORT -----------------
