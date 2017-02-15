# MAIN CLASS

from robo_surface import RoboSurface
from robo_utils import ValidateInput

# Boolean to identify PLACE Command
PLACE_FLAG = False

validateSession = ValidateInput()
surface = RoboSurface()

for case in validateSession.ENTERED_COMM:
    print(case)
    if case.startswith('PLACE'):
        t1 = case.split(' ')[1]
        RoboSurface.place(surface, int(t1.split(',')[0].strip()),int(t1.split(',')[1].strip()),t1.split(',')[2].strip())
        if not PLACE_FLAG:
            PLACE_FLAG = True
    elif case.strip() == 'MOVE':
        RoboSurface.move(surface)
    elif case.strip() == 'LEFT':
        RoboSurface.move(surface)
    elif case.strip() == 'RIGHT':
        RoboSurface.right(surface)
    elif case.strip() == 'REPORT':
        RoboSurface.report(surface)
