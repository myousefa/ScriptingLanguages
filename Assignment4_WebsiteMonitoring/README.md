# Assignment 4 : Website Monitoring

Authors: Mohammed Ali

Class: CSS 390 - Scripting Languages

Professor: Dr.Morris Bernstein

Language: Python3 

## Project Description

The purpose of this project is to delve further into python scripting. In this project, the goal was to build a website that send traffic to it and monitor how it handles the requests. It also builds on the foundations using the math.lib library built into python. This will be handy in industry as it is a frequently used library. The following sections will mention implementation details so be sure to read on to understand the project in more depth and how I implemented it. 

### Part 1 : Traffic Generator
For the traffic generator, I used a while loop to make constant requests to the server. Using urllib2 I used the .open() func to make a 1 in 10 chance of accessing 404 error or 500 error. I had an 80% chance of a successful run. I knew this would only output linear growth but it was enough to move on to part two. 

### Part 2 : Stats Collector
For the stats collector I used a tsv file and using built in python functions to add data in. This required scraping the `http://localhost:8080/stats` every 10 seconds. To do this, I had a counter that counted down each time data was added. Once that counter ran down to 0 it stops scraping data and stops adding to the tsv file. 

### Part 3 : Dashboard
This part arguebaly challenged me the most. I was havinng trouble modifying my data to to be suited for the rps per minute standard. This took me a while to modify and worked best when i used numpy style arrays as they allowed me to modify array data a lot easier. 

## Test Data
There is a folder called example stuff, which consists of `data_example.tsv`. This was my data after letting my generator collect data for an hour. There is also my `graph.png`. 

# How to Run 
Start by running `./run.sh` for desired amount of time. Once you have ran for more than 20 minutes enough data has been collected, press control+c to exit out of it. Next run `./vis.sh`. This will plot the data and output `graph.png`.