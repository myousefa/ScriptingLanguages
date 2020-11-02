# Assignment 2 : Media Server

Authors: Mohammed Ali

Class: CSS 390 - Scripting Languages

Professor: Dr.Morris Bernstein

## Project Description

This project extends upon the first project. In this project we were to create a script to generate an HTML file that hosts a table of artists, their albums, and lastly the tracks for that album. Part of the project was to do this using two languages from the choices listed below: 

1. Pure Bash
2. Awk
3. Perl
4. Python 

I choose to do my implementations in Python and Perl.

### Part 1 (Python)
The first part of the project was to create an input file. To do this I created a python file that breaks down the music directory and all its contents. Once done, I passed the `input.txt` file into my main file called `gen_html.py.`

The simple breakdown of this code starts with creating the data structure to hold the artists, albums, and tracks. To do this I created a Map that as a Key stores the artist, and as its value holds another hashmap. This hasmap has a Key that stores the albums. The value is an array that holds all the tracks. 

Once all the input is gathered and stored into the data structure all that was left was to worry about the html formatting and other small challenges. The one challenge I ran into was getting the rowspan for the number of albums, and getting the overall correct table format.

See comments in code for specific notes on the implementation.

NOTE: The JSON file was for me the developer of this code to help visualize the data structure build. 

### Part 2 (Perl)
The algorithm works very similar to the python solution. However creating the data strcuture and the overall implementation was significanntly more work and took a lot longer. 

See comments in code for specific notes on the implementation.

## Test Data

The test data I created tests files with no OGG files in it. It also tests how it deals with if an artist shows up with more than two disks. It also sees if it handles if one disk is "disk" while the other is "disc." Another test is to see how it handles cross genre multi disk scenarios. Overall the program handled all these situations in an appropriate manner. I did not include files for expected output for these but it is easy to run since it is given as a tar file. 

# How to Run 

To run this program ensure that the python and perl files are adjacent to the music directory. If it inside along with the genres it will not run successfully. In ubuntu or MacOS terminal run `python3 gen_html.py`. This will give you the expected result as seen in the `output.html` file. 

For the Perl file run the script `./gen_html.sh` script to get the output in the `output.html` file.