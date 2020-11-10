#! /usr/bin/env bash

#Problem3
#  For each directory in the subtree rooted at the current directory, 
#  makes sure only the owner has read, write, or execute permission
#  (a directory must be “executable” in order to be able to use it 
#  in a path).That is, Hint: use find with -exec flag or find -print0 
#  and xargs -0.

find . -type f -print0 | xargs -0 sudo chmod go-rwx | echo "DONE"
