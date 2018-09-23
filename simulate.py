"""
Define valid face directions for robot as key/value pairs

Key => Face Direction
Value => Tuple containing valid left and right directions for corresponding key
 [0] => current  x,y co-ordinates then return the NEW x,y co-ordinates according to the robot's move
 [1] => New direction after turning LEFT
 [2] => New direction after turning RIGHT
"""
pos_directions = {'NORTH' : (lambda x, y: (x, y + 1), "WEST", "EAST"),
                    'EAST' : (lambda x, y: (x + 1, y), "NORTH", "SOUTH"),
                    'SOUTH' : (lambda x, y: (x, y - 1), "EAST", "WEST"),
                    'WEST' : (lambda x, y: (x - 1, y), "SOUTH", "NORTH")}

class Robot():
    """
    '''
    Robot class - Represents toy robot entity.

    @param x: x co-ordinate of toy robot. Defaults to 0
    @param y: y co-ordinate of toy robot. Defaults to 0
    @param facing: direction toy robot is facing to. Defaults to (NORTH).
    '''
    """

    facing = ""
    x = 0
    y = 0

    def __init__(self,x=0,y=0,facing="NORTH"):

        self.facing = facing
        self.x = x
        self.y = y
    
    def get_position(self):
        """
        :return: current co-ordinates of the toy robot (x co-ordinate, y co-ordinate)
        """

        return (self.x, self.y)
    
    def set_position(self,x=0,y=0):
        """
        Sets the current co-ordinates of the toy robot.
        :param x: x co-ordinate of the toy robot
        :param y: y co-ordinate of the toy robot
        :return: None
        """

        self.x = x
        self.y = y
    
class Tabletop():
    """
    Tabletop class - Represents a tabletop entity

    @param x_limit: maximum limit of x co-ordinate. Defaults to (5)

    @param y_limit: maximum limit of y co-ordinate. Defaults to (5)
    @param robot: The toy robot object that has been placed onto the table top
    @param flag: Boolean flag value denoting the toy robot presence on the table. (Defaults to False)

    """

    x_limit = 0
    y_limit = 0
    robot = None
    flag = False

    def __init__(self,x_limit=5,y_limit=5):
        """
        Build tabletop object - Defaults are 5x5
        :param x_limit: maximum limit for x co-ordinate
        :param y_limit: maximum limit for y co-ordinate
        """

        self.x_limit = x_limit
        self.y_limit = y_limit

    def print_usage(self,helpfile):
        """

        Prints usage/help for the application
        :param readfile: file which has usage information
        :return: None
        """
        with open(helpfile, 'r') as readfile:
           help_content = readfile.read()
           print help_content

    def _valid_move(self,x,y):
        """
        Check if input command is valid or not
        :param x:
        :param y:
        :return: Boolean value
        """

        if self.x_limit > x >= 0 and self.y_limit > y >= 0:
            return True
        else:
            return False
    
    def place(self,x=0,y=0,facing="NORTH"):
        """
        Place toy robot onto a specified tabletop location

        Defaults are x position 0, y position 0 and facing North

        :param x: x-coordinate on the tabletop
        :param y: y-coordinate on the tabletop
        :param f: facing direction of toy robot
        :return: None
        """

        try:
            x = int(x)
            y = int(y)
        except ValueError:
            return "Invalid co-ordinates"

        if facing.upper() not in pos_directions:
            return "Invalid direction , must be %s " % " ".join(pos_directions.keys().sort())

        if not self._valid_move(x,y):
            return "Invalid x,y co-ordinates , must be between 0 and 5 "

        self.robot = Robot(x,y,facing.upper())
        self.flag = True
    
    def move(self):
        """
        Move the robot, as per the current position and direction
        :return: String conditionally
        """

        if not self.flag:
            return "Use PLACE command first to place robot on the table"
        
        move_to = pos_directions[self.robot.facing][0]
        new_pos = move_to(*self.robot.get_position())

        if self._valid_move(*new_pos):
            self.robot.set_position(*new_pos)
        else:
            return "Move ignored as Robot will fall off the table."
    
    def left(self):
        """
        Turn toy robot left
        :return: String conditionally
        """

        if not self.flag:
            return "Use PLACE command first to place robot on the table"
        new_direction = pos_directions[self.robot.facing][1]
        self.robot.facing = new_direction
    
    def right(self):
        """
        Turn toy robot right
        :return: String conditionally
        """

        if not self.flag:
            return "Use PLACE command first to place robot on the table"
        new_direction = pos_directions[self.robot.facing][2]
        self.robot.facing = new_direction
    
    def report(self):
        """
        :return: return current toy robot position
        """

        if not self.flag:
            return "Use PLACE command first to place robot on the table"
        x, y = self.robot.get_position()
        return "%i,%i,%s" % (x , y , self.robot.facing)


