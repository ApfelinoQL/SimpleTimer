import time
import GUI
def Countdown(MT,ST):
    while MT > -1 and ST > -1:
        if ST >=10:
            print(str(MT) + ":" + str(ST))
            GUI.MinuteSTimeleft(MT,ST)
        else:
            print(str(MT) + ":0" + str(ST))
            GUI.MinuteSTimeleft(MT, ST)
        if ST == 0:
            MT -= 1
            ST = 60
        ST -= 1
