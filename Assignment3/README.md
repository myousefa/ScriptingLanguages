# Assignment 3 : Log Analysis

Authors: Mohammed Ali

Class: CSS 390 - Scripting Languages

Professor: Dr.Morris Bernstein

Language: Python3 

## Project Description

This program reads in two log files and converts it into four dictionaries. The dictionaries information will be compared and find keys that have missing or added values. After doing this it will output a report of all this information. 

Sounding simple to get started by spliting the project into two parts. Read further on what each part consisted of. 

### Part 1 : Get Summary
The first part of the project was creating the dictionaries and outputting the summary that had the following information: 

1. total cookies in baseline
2. empty cookies in baseline
3. non-empty cookies in baseline
4. total cookies in test
5. empty cookies in test
6. non-empty cookies in test
7. non-empty cookies in baseline only
8. non-empty cookies in test only
9. non-empty cookies in both
10. non-empty cookies in either

This process was quite easy and just consisted of getting all the information into the map and doing basic calculations based on the len of the map and setting to the appropriate information

### Part 2 : Final Report
The second part of the project took a lot more time and more testing. In this part after filling the maps I created a method that does a series of checks. They checked for: 

1. Segments with added cookies
2. Segments with missing cookies
3. Cookies in extra segments
4. Cookies omitted from segments

## Test Data

For test data I took a small subset of the provided data and put it into the .log files

# How to Run 
To run the program in command line run `python3 gen.py evaluator-integration-baseline.log evaluator-integration.log > example.txt`

NOTE: `baseline.log` file MUST come before the comparison .log file
NOTE2: `example.txt` file can be compared to my expected output stored in `report.txt`. 