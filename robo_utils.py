

# LIST OF VALID COMMANDS

class RoboUtils(object):

    # constructor
    def __init__(self, x=0, y=0, op_side="NORTH"):
        self.side = op_side
        self.x_ax = x
        self.y_ax = y

    def set_position(self, x=0, y=0):
        self.x_ax = x
        self.y_ax = y

    def get_position(self):
        return self.x_ax, self.y_ax

    def set_facing(self, op_side):
        self.side = op_side

    def get_facing(self):
        return self.side

class ValidateInput(object):
    VALID_COMMANDS = ['PLACE', 'MOVE', 'LEFT', 'RIGHT', 'REPORT']
    ENTERED_COMM = []
    file = open('O:/input.txt', 'r')
    for line in file:
        flag = line.split(" ")[0].strip().upper() in VALID_COMMANDS
        if flag:
            ENTERED_COMM.append(line.upper())

    file.close()