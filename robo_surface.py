from robo_utils import RoboUtils


class RoboSurface(object):
    surface_x = 0
    surface_y = 0
    robo_t1 = None
    robo_placed = False

    def place(self, x=0, y=0, facing="NORTH"):
        x_ax , y_ax = int(x) , int(y)
        self.robo_t1 = RoboUtils(x, y, facing.upper())
        self.robo_placed = True

    def report(self):
        if not self.robo_placed:
            return "Cannot perform report. Robot not placed yet."
        x, y = self.robo_t1.get_position()
        return x , y , self.robo_t1.facing














