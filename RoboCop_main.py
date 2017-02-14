from Table import TableTop

# LIST OF VALID COMMANDS
VALID_COMMANDS = ['PLACE', 'MOVE', 'LEFT', 'RIGHT', 'REPORT']
ENTERED_COMM = []
# LOADING FILE (HARDCODED)
file = open('O:/input.txt', 'r')
for line in file:
    #print(line)
# EXTRACT FIRST KEYWORD FROM FILE TO VALIDATE
    flag = line.split(" ")[0].strip() in VALID_COMMANDS
    print(ENTERED_COMM)
    print(flag)
    if flag:
        ENTERED_COMM.append(line)
        for i in ENTERED_COMM:
            print('list created : ' + i)
            print(len(ENTERED_COMM))
    else:
        print('list of Valid commands are : ', end=' ')
        for i in VALID_COMMANDS:
            print(i, end=',')
        break
# close the flag
file.close()