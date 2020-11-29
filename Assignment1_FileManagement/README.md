# Assignment 1 : File Management

Authors: Mohammed Ali

Class: CSS 390 - Scripting Languages

Professor: Dr.Morris Bernstein

## Project Description

This project teaches the fundamnetals of bash scripting. Including experience with pipelining commands, sed, awk, and Perl. 

In the project there is a music directory filled with Genres, artists, album names, dis[c][k]s, and songs. The objective of this is to do the following:

### Part 1 (WarmUp)
Using bash scripts to get a report of the following information:

1. total number of tracks
2. number of distinct artists/bands
3. artists who have albums in more than one genre (in alphabetical order)
4. multi-disk albums (in alphabetical order)

No sed, awk, Perl, or Python in this section was used

### Part 2 (Detailed Report)
Using bash scripts to get a more detailed report of 

1. artists who have albums in more than one genre (in alphabetical order)
    - With genres listed below the artists
2. multi-disk artists and the albums listed below (in alphabetical order)
3. Possible Duplicated Albums

I used sed in third part. This was to ensure proper spacing. No awk, Perl, or Python were used in this project. 

## Test Data

The test data I created tests files with no OGG files in it. It also tests how it deals with if an artist shows up with more than two disks. It also sees if it handles if one disk is "disk" while the other is "disc." Another test is to see how it handles cross genre multi disk scenarios. Overall the program handled all these situations in an appropriate manner. I did not include files for expected output for these but it is easy to run since it is given as a tar file. 

# How to Run 

To run this program ensure that the shell files are adjacent to the music directory. If it inside along with the genres it will not run successfully. In ubuntu or MacOS terminal run `./warmup.sh` or `./detailed.sh`. 

This will give you the expected result as seen in the `WarmupOutput.txt` file and `DetailedOutput.txt` file.