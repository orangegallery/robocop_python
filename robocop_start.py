# MAIN CLASS

from robo_surface import RoboSurface
from robo_utils import RoboUtils

# LIST OF VALID COMMANDS
VALID_COMMANDS = ['PLACE', 'MOVE', 'LEFT', 'RIGHT', 'REPORT']
ENTERED_COMM = []
# LOADING FILE (HARDCODED)
file = open('O:/input.txt', 'r')
for line in file:
    # print(line)
    # EXTRACT FIRST KEYWORD FROM FILE TO VALIDATE
    flag = line.split(" ")[0].strip() in VALID_COMMANDS
    print(ENTERED_COMM)
    print(flag)
    if flag:
        ENTERED_COMM.append(line)
    else:
        print('list of Valid commands are : ', end=' ')
        for i in VALID_COMMANDS:
            print(i, end=',')
            break
# close the flag
file.close()

print("Surface started")
surface = RoboSurface()
RoboSurface.place(surface, 0, 0, 'NORTH')

t5 = RoboSurface.report(surface)
print(t5)

RoboSurface.move(surface)
RoboSurface.move(surface)
print('report1')
print(RoboSurface.report(surface))
#RoboSurface.move(surface)
RoboSurface.left(surface)
RoboSurface.move(surface)
RoboSurface.left(surface)
RoboSurface.move(surface)

print("sleep")

t5 = RoboSurface.report(surface)
print('final report')
print(t5)
