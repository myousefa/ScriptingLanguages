# Midterm Review 

Authors: Mohammed Ali

Class: CSS 390 - Scripting Languages

Professor: Dr.Morris Bernstein

## Description

This is file to practice some of the skills I have learned thus far. Each of these problems reiterate some of the skills I have learned and push me towards mastery. 

### Questions
1. List every file in the current directory that is not executable but contains a #! line. Hint: use the test or [ (left square bracket) commands. Add execute permission to those files.

2. Find all awk scripts under the current directory and change the #! line from /usr/local/bin/gawk to /usr/bin/gawk

3. For each directory in the subtree rooted at the current directory, makes sure only the owner has read, write, or execute permission (a directory must be “executable” in order to be able to use it in a path).That is, Hint: use find with -exec flag or find -print0 and xargs -0.

4. Download a randomly-selected C or C++ project from github or similar repository, e.g. Linux kernel, Bash, nethack (game). For each .h file, list the header and source files that #include it. Hint: generate a collection of files included-by each source and reorder the data.

5. Write a script that creates some files and directories in a directory tree below the current directory. The files and directories should have spaces in their names (use mkdir to create directories and touch to create zero-length files).
        
        Write a script to rename the paths to remove spaces or replace them with underscores. Make sure no file gets "overwritten" by another on (e.g. both "ab c" and "a bc" map to abc). Make sure your data generator script has cases that test this.
        Write a script that generates a script containing the required mv commands with whatever control logic is required to avoid clobbering files. Verify the generated script works correctly.

6. 

## Test Data
I created the test data to check if the scripts actually worked. 

# How to Run 

To run these programs all that needs to be done is ./`FILENAME`. Each file is labeled with the associated question number. 