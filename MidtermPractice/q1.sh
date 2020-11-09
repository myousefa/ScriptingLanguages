#! /usr/bin/env bash

# Problem1
#  List every file in the current directory that is not executable but contains a #! line. Hint: use the
#  test or [ (left square bracket) commands. Add execute permission to those files.


# ----------- FIRST ATTEMPT -----------
# for i in * ; do
#     if test -x "$i" ; then 
#         continue 
#     fi
#     if egrep '^#!' "$i" ; then
#         echo "$i"
#         sudo chmod a+x "$i"
#     fi
# done

# ----------- WORKING SOLUTION -----------
ls -1 | 
while read i ; do 
     test -f "$i" && head -1 "$i" | 
    egrep -qs '^#!' && chmod a+x "$i" | 
    echo "$i"; 
done
