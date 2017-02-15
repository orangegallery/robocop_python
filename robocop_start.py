# MAIN CLASS
import sys
from robo_surface import RoboSurface
from robo_utils import ValidateInput

# Boolean to identify PLACE Command
PLACE_FLAG = False

# Check the length of the arguments and validate
if len(sys.argv) <= 1:
    print("file path not found!")
    print("USAGE : <program name> <Command text file path>")
    exit()

# validate input class insta
validateSession = ValidateInput()
# Surface class insta
surface = RoboSurface()
# Valdating text and formatting
ValidateInput.processfile(validateSession, sys.argv[1])
# ValidateInput.processfile(validateSession, "O:/input.txt")
# Move robot based on the saved commands list in ENTERED_COMM in Validate session class
for case in validateSession.ENTERED_COMM:
    if case.startswith('PLACE'):
        t1 = case.split(' ')[1] # temp variable to avoid line is too big warning on the next line
        RoboSurface.place(surface, int(t1.split(',')[0].strip()),int(t1.split(',')[1].strip()),t1.split(',')[2].strip())
        if not PLACE_FLAG: # Check if Place flag is already set?
            PLACE_FLAG = True # Setting the PLACE flag to true
    elif PLACE_FLAG and case.strip() == 'MOVE':  # MOVE only if PLACE flag is true and command matches to 'MOVE'
        RoboSurface.move(surface)
    elif case.strip() == 'LEFT' and PLACE_FLAG:  # MOVE left only if PLACE flag is true and command matches to 'LEFT'
        RoboSurface.left(surface)
    elif case.strip() == 'RIGHT' and PLACE_FLAG:  # MOVE right only if PLACE flag is true and command matches to 'RIGHT'
        RoboSurface.right(surface)
    elif case.strip() == 'REPORT' and PLACE_FLAG:  # Print report only if PLACE flag is true & command matches 'REPORT'
        RoboSurface.report(surface)
