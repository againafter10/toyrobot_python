""""
Created on 04/10/2017

@summary: Toy Robot Simulator for DealMax
@author: Archana Joshi
@version: 1.0

"""

from entities import Tabletop
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
    #table.print_usage()  //dispaly usage of the application
    print "================================================="
    print "Enter commands as PLACE(...),RIGHT,LEFT,MOVE,REPORT"
    print "PLACE command with arguments (PLACE x,y,f) "
    print "the following commands: RIGHT, LEFT, REPORT, MOVE."
    print "Press enter to exit. Otherwise begin by using the"
    print "================================================="
    
    while True:
        input = raw_input('Command: ')
        if not input: raise SystemExit
        input = input.split(' ')
        try:
            try:
                command, args = input[0], input[1].split(",")
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", metavar="File",default="",nargs="?",
                               help="Optional input file with each command on a new line ")
    

    args = parser.parse_args() #Collect the command-line arguments

    if args.i:
        with_input_file(args.i)
    else:
        no_input_file()

if __name__ == '__main__':
    main()