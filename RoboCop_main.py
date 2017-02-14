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

t1 = RoboUtils()
#RoboUtil.set_position(t1, 0, 2)
t2, t5 = RoboUtils.get_position(t1)
t3 = RoboUtils.get_facing(t1)
print(t2)
print(t3)
print(t5)

print("Surface started")
surface = RoboSurface()
t4 = RoboSurface.place(surface, 2, 6, 'SOUTH')
print(t4)
print("sleep")
