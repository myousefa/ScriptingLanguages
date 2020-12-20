# Assignment 5 : Finite-State-Machine Generator

Authors: Mohammed Ali

Class: CSS 390 - Scripting Languages

Professor: Dr.Morris Bernstein

Language: Python3 

## Project Description

This project utilizes the built in fsm features of python. The idea of the project is to use graph topics and Domain Specific Languages to generate C++ file to create said FSM. 

### Part 1 : Main.py
The first part of this project is to utlize the given code from professor to create some headers, footers, and other specific features of the fsm. Main.py implements the needed boiler plate utilized in the program.

### Part 2 : fsm.py
The second part of this project is to utilize code written in class and continue to build off of the given code. For this section I implemented the string to event method and rewrote much of the main hos function. The hos function is the main logic behind the FSM. 

### Part 3 : Main_Float.py & Float_output.cpp
These code segments are the final part of the project. This part was pretty easy as all I had to do was run the main_float file and it output a cpp file. It utilizes fsm.py as the logic carries over to this part of the project. 

## Test Data

`hos.cpp` is my example output for part 2 of the project. `float_output.cpp` is my output part part 3 of this project No data was needed for this project.

# How to Run 

To run my program first run `python3 main.py > hos.cpp` then run `g++ -c hos.cpp` into the terminal. The first will run and add C++ code into `hos.cpp`. After this generation is done you must compile the code and the latter command will do this using g++. Ensure g++ interpreter is downloaded onto you PC. Clang may work as well.

To run the other part is quite simple run, `python3 main_float.py` then `g++ -c float_output.cpp`.