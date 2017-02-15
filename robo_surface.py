from robo_utils import RoboUtils

dict_calc = {
                'NORTH': (lambda x, y: (x, y + 1), "WEST", "EAST"),
                'SOUTH': (lambda x, y: (x, y - 1), "EAST", "WEST"),
                'EAST': (lambda x, y: (x + 1, y), "NORTH", "SOUTH"),
                'WEST': (lambda x, y: (x - 1, y), "SOUTH", "NORTH")
            }


class RoboSurface(object):
    surface_x = 0
    surface_y = 0
    robo_t1 = None

    # constructor
    def __init__(self, x=5, y=5, op_side="NORTH"):
        self.surface_x = x
        self.surface_y = y

    def place(self, x=0, y=0, op_side="NORTH"):
        x_ax, y_ax = int(x), int(y)
        self.robo_t1 = RoboUtils(x, y, op_side)

    def report(self):
        x, y = self.robo_t1.get_position()
        print(x, y, self.robo_t1.side)

    def _valid_move(self, x, y):
        if self.surface_x > x >= 0 and self.surface_y > y >= 0:
            return True
        else:
            return False

    def move(self):
        move_func = dict_calc[self.robo_t1.get_facing()][0]
        new_pos = move_func(*self.robo_t1.get_position())
        if self._valid_move(*new_pos):
            self.robo_t1.set_position(*new_pos)

    def left(self):
        new_direct = dict_calc[self.robo_t1.get_facing()][1]
        self.robo_t1.set_facing(new_direct)

    def right(self):
        new_direct = dict_calc[self.robo_t1.get_facing()][2]
        self.robo_t1.set_facing(new_direct)










