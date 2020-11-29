#! /bin/bash

#Problem2


echo "----------------- Part A ----------------------"

ls -1 |
while read i; do
    test -f "$i" && head -1 "$i" |
    # while reading through each file get the files that consist of the shebang and trim it out
    egrep '^#!' | tr -d '#! ' | 
    while read line
    do  
        # checking if interpreter exists or not
        if [ -e "$line" ]; then 
            continue;
        elif [ ! -e "$line" ]; then
            echo "MISSING:" "$line"
        fi
    done
    
done

echo "----------------- Part B ----------------------"
ls -1 |
while read i; do
    test -f "$i" && head -1 "$i" |
    # while reading through each file get the files that consist of the shebang and trim it out
    egrep '^#!' | tr -d '#! ' | 
    while read line
    do
        # checking if interpreter exists or not and returning with the associated file name  
        if [ -e "$line" ]; then 
            continue;
        elif [ ! -e "$line" ]; then
            echo "MISSING INTERPRETER:" "$line" "@" "$i"
        fi
    done
    
done