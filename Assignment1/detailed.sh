#!/bin/bash

# ---------------- DETAILED REPORT -----------------
echo -e "Multi Genre Artists: " 
# gets the multi genre artists
find -mindepth 3 -maxdepth 3 -printf '%f\n' | sort | uniq -d |
# each time it gets an artists do the following  
while read artists; do 
    echo "  $artists"
    # gets the genres
    find -iname "*$artists*" | cut -d/ -f 3 | sort | uniq |
    while read genres; do
        echo "      $genres"
    done
done
echo

echo -e "Multi Disk Albums: "
# gets the multi disk artists 
find -mindepth 5 -maxdepth 5 -iname "dis??" | cut -d / -f 4 | sort | uniq -d |
while read artists; do
    echo "  $artists"
    # gets the multi disk album name
    find -mindepth 5 -maxdepth 5 -iname "dis??" | grep "$artists" | cut -d / -f 5 | sort | uniq |
    while read albums; do
        echo "       $albums"
    done
done
echo

echo -e "Possible Duplicate Albums: "
# gets the album found in multiple places
find -mindepth 4 -maxdepth 4 -type d | cut -d/ -f 5 | sort | uniq -d | 
while read albums; do
    echo "  $albums"
    # gets the different artists and genres
    # using sed command to parse the words to get rid of '/' and replace with ' '
    find -mindepth 4 -maxdepth 4 -type d -iname "$albums" | cut -d/ -f 3,4 | sed 's|/| |g' |sort -k 2| 
    while read all; do
        echo "      $all"
    done
    # echo each time to add sspace between each album
    echo
done
exit
# ---------------- DETAILED REPORT -----------------
