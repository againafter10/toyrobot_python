""""
Created on 04/10/2017
Toy Robot Simulator

This application is a simulation of a toy robot moving on a square tabletop,of dimensions 5 units x 5 units.

There are no other obstructions on the table surface and the robot is free to roam around the surface of the table.
The robot however must be prevented from falling off the table boundary.

@summary: Toy Robot Simulator
@author: Archana Joshi
@version: 1.0

"""

from simulate import Tabletop
import argparse


def with_input_file(input_file):
    """
    Runs commands from a specified input file.
    """

    table = Tabletop() #Initiate to a 5X5 tabletop object.
    try:
        with open(input_file, 'r') as readfile:
            line_count = 1
            for line in readfile.readlines():
                input = line.rstrip().split(' ')
                try:
                    try:
                        command, args = input[0], input[1].split(",")
                    except IndexError:
                        command = input[0]
                        args = ()
                    result = getattr(table, command.lower())(*args)

                    if result: print result
                except (AttributeError, TypeError):
                    print 'Invalid command on line: %i - Skipped this line and continued processing' % line_count
                finally:
                    line_count += 1
    except IOError:
        print "No file found '%s' found. Ensure it exists and is readable." % input_file

def no_input_file():
    """
    Run the application without an input file - Displays command prompt
    """

    table = Tabletop() #Initiate to a 5X5 tabletop object.
    table.print_usage('usage_file')  #dispaly usage of the application
    prompt = ''
    while prompt not in ('Y','y'):
        prompt = raw_input("Are you ready for the commands(Y/N)? ")


    while True:
        input = raw_input('New Command: ')
        if not input: raise SystemExit
        input = input.split(' ')
        try:
            try:
                command = input[0]
                args =  input[1].split(",")
            except IndexError:
                command = input[0]
                args = ()
            result = getattr(table, command.lower())(*args)
            if result: print result
        except (AttributeError, TypeError):
            print 'Invalid Command!'

def main():
    """
    Main function
    
    Parses and collects optional command line arguments (Such as the command input file)
    then executes the application as per commands given
    """
    parser = argparse.ArgumentParser(description="Collect the command-line arguments")
    parser.add_argument("-i", metavar="File", nargs="?",
                        help="Optional input file with each command on a new line")

    # Collect the command-line arguments
    args = parser.parse_args()
    if args.i:
        with_input_file(args.i)
    else:
        no_input_file()


if __name__ == '__main__':
    main()