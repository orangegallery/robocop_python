# MAIN CLASS

from robo_surface import RoboSurface
from robo_utils import ValidateInput

# Boolean to identify PLACE Command
PLACE_FLAG = False

validateSession = ValidateInput()
surface = RoboSurface()

for case in validateSession.ENTERED_COMM:
    if case.startswith('PLACE'):
        t1 = case.split(' ')[1]
        RoboSurface.place(surface, t1.split(',')[0].strip(),t1.split(',')[1].strip(),t1.split(',')[2].strip())
        if not PLACE_FLAG:
            PLACE_FLAG = True
    if case('MOVE'):
        RoboSurface.move(surface)
    if case('LEFT'):
        RoboSurface.move(surface)
    if case('RIGHT'):
        RoboSurface.right(surface)
    if case('REPORT'):
        RoboSurface.report(surface)

exit()
print("Surface started")








t5 = RoboSurface.report(surface)
print(t5)

RoboSurface.move(surface)
RoboSurface.move(surface)
# RoboSurface.move(surface)
# RoboSurface.left(surface)
# RoboSurface.move(surface)
RoboSurface.left(surface)
RoboSurface.move(surface)

print("sleep")

t5 = RoboSurface.report(surface)
print('final report')
print(t5)