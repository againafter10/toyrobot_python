#######################
Toy Robot Simulator

This application is a simulation of a toy robot moving on a square tabletop,of dimensions 5 units x 5 units.
There are no other obstructions on the table surface and the robot is free to roam around the surface of the table.
The robot however must be prevented from falling off the table boundary.

@author: Archana Joshi
@version: 1.0
#######################


Usage

execute the main.py python script from the command line as follows:

   python main.py

To exit the application while in command mode at any time simply leave the input blank and hit 'Enter'.

Entering the PLACE command without any arguments will place the robot at the origin with the default facing position .
These defaults are the position (0,0) facing NORTH


Alternate Usage

A text file can also be used as an input for a series of instructions with each instruction on a separate line.

execute the main.py python script specifying the absolute path of the input file from the command line as follows:

  python main.py -i LOCATION_OF_FILE
