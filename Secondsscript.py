import time
import GUI
def Countdown(Time):
    while Time > -1:
        if Time >= 10:
            print("0:" + str(Time))
            GUI.SecondSTimeleft(Time)
        else:
            print("0:0" + str(Time))
            GUI.SecondSTimeleft(Time)
