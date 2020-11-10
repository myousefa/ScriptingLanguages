#! /usr/bin/env bash

#Problem4
#  Download a randomly-selected C or C++ project from github or similar repository, e.g. Linux kernel, Bash, nethack (game). 
#  For each .h file, list the header and  sourcefiles that #include it. 
#  Hint: generate a collection of files included-by each source and reorder the data.

# Look in directory for .h file
# find . -name "*.h" -print | for $FileName in *; do 

# Look inside .cpp files for if grabbed .h file includes it
    # find. - name "*.cpp" -print | for $CPPFile in *; do
    #     while read $CPPFile; do
    #         if 

# Print the headername and cpp file that includes it




find . \( -name '*.h' -o -name '*.cpp' \) -print0 | 
xargs -0 egrep -nH '#include' |
sed -e 's/:[^<"]*[<"]/:/;s/[>"].*//'
