

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


