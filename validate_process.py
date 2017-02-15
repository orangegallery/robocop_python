class ValidateInput(object):
    VALID_COMMANDS = ['PLACE', 'MOVE', 'LEFT', 'RIGHT', 'REPORT']
    ENTERED_COMM = []
    lines = []

    def processfile(self, file_name):
        try:
            with open(file_name) as f:
                lines = f.readlines()
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            exit()
        for line in lines:
            t2 = line.split(" ")[0].strip().upper()
            flag = t2 in ValidateInput.VALID_COMMANDS

            if t2 == 'PLACE':  # If block to check the correct place command
                t3 = line.split(" ")[1].split(',')
                if not ((len(t3) == 3) and (t3[0].isdigit()) and (t3[1].isdigit()) and (len(t3[2].strip()) == 4)):
                    # Disabling the print because requirement says ignore invalid commands
                    # print(line.strip(), ' - command is not recognised by Robocop')
                    # print('Update the correct PLACE command and try again')
                    exit()

            # Formatting of place command in text file. desired format PLACE 1,2,3
            if flag:
                ValidateInput.ENTERED_COMM.append(line.upper())
        f.close()