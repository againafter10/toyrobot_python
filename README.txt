
# -------------------------------------------------------------------------
#  DATE:  October 4, 2017
#
#  Toy Robot Simulator - Version: 1.0
#  This application is a simulation of a toy robot moving on a square tabletop,of dimensions 5 units x 5 units.
#  There are no other obstructions on the table surface and the robot is free to roam around the surface of the table.
#  The robot however must be prevented from falling off the table boundary.
#
#  -----------------------------------------------------------------
#  Software/Tools Used
#  -----------------------------------------------------------------
#  Operating System : Darwin 15.6.0 x86_64
#  Language : Python 2.7.13
#
#
#  -----------------------------------------------------------------
#  Constraints/Assumptions
#  -----------------------------------------------------------------
#  - allowed multiple PLACE commands as input.
#  - input file can be empty(No result in that case)
#  - given commands are not case specific
#
#  -----------------------------------------------
#  Usage Instructions
#  -----------------------------------------------
#
#  execute the main.py python script from the command line as follows:
#
#  python main.py
#
#  To exit the application while in command mode at any time simply leave the input blank and hit 'Enter'.
#
#  Entering the PLACE command without any arguments will place the robot at the origin with the default
#  facing position .These defaults are the position (0,0) facing NORTH
#
#  Alternate Usage
#  ----------------
#
#  A text file can also be used as an input for a series of instructions with each instruction on a separate line.
#
#  execute the main.py python script specifying the absolute path of the input file from the command line as follows:
#
#  python main.py -i LOCATION_OF_FILE
#
#
#  -----------------------------------------------
#  Folder/File Description
#  -----------------------------------------------
#
#     toyrobot_python
#         |
#         |__README.txt
#         |
#         |__screenshots(d)
#         |
#         |__main.py
#         |
#         |__simulate.py
#         |
#         |__test(d)
#         |
#         |__usage_file
#
#
#  1. toyrobot_python - enclosing folder
#
#  2. README.txt - contains generic information about other files in the folder and usage of the application
#
#  3. screenshots - directory containing application execution screenshot for some usecases.
#
#  4. main.py - main driver file
#
#  5. simulate.py - core methods
#
#  6. test - directory containing test input files
#
#  7. usage_file - help/usage details
#
#